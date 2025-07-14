from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile, UserRole

class CustomAccountAdapter(DefaultAccountAdapter):
    """Custom account adapter for allauth"""
    
    def get_login_redirect_url(self, request):
        """Redirect to dashboard after login"""
        return '/accounts/dashboard/'
    
    def get_logout_redirect_url(self, request):
        """Redirect to home after logout"""
        return '/'

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """Custom social account adapter for allauth"""
    
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed
        """
        pass
    
    def save_user(self, request, sociallogin, form=None):
        """
        Saves a newly signed up social login. In case of auto-signup,
        this will be called on sociallogin but not on form
        """
        user = super().save_user(request, sociallogin, form)
        
        # Get or create user profile
        profile, created = UserProfile.objects.get_or_create(user=user)
        
        if created:
            # Set default role for social login users
            profile.role = UserRole.USER
            profile.is_verified = True  # Consider social accounts as verified
            
            # Extract additional info from social account
            if sociallogin.account.provider == 'google':
                extra_data = sociallogin.account.extra_data
                # Google provides name in different format
                if not user.first_name and 'given_name' in extra_data:
                    user.first_name = extra_data.get('given_name', '')
                if not user.last_name and 'family_name' in extra_data:
                    user.last_name = extra_data.get('family_name', '')
                    
            elif sociallogin.account.provider == 'facebook':
                extra_data = sociallogin.account.extra_data
                # Facebook provides first_name and last_name
                if not user.first_name and 'first_name' in extra_data:
                    user.first_name = extra_data.get('first_name', '')
                if not user.last_name and 'last_name' in extra_data:
                    user.last_name = extra_data.get('last_name', '')
                    
            elif sociallogin.account.provider == 'twitter':
                extra_data = sociallogin.account.extra_data
                # Twitter provides name as a single field
                if not user.first_name and 'name' in extra_data:
                    name_parts = extra_data.get('name', '').split(' ', 1)
                    user.first_name = name_parts[0]
                    if len(name_parts) > 1:
                        user.last_name = name_parts[1]
            
            user.save()
            profile.save()
        
        return user
    
    def get_connect_redirect_url(self, request, socialaccount):
        """
        Returns the default URL to redirect to after successfully
        connecting a social account.
        """
        return '/accounts/profile/'
