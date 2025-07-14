from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from django.conf import settings


class Command(BaseCommand):
    help = 'Test social authentication setup'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Testing Social Authentication Setup...\n')
        
        # Check site configuration
        site = Site.objects.get(pk=1)
        self.stdout.write(f'📍 Site: {site.domain} ({site.name})')
        
        if site.domain != 'localhost:8000':
            self.stdout.write(self.style.WARNING('⚠️  Site domain should be localhost:8000 for development'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ Site domain configured correctly'))
        
        # Check social apps
        self.stdout.write('\n🔐 Social Applications:')
        providers = ['google', 'facebook', 'twitter']
        
        for provider in providers:
            try:
                app = SocialApp.objects.get(provider=provider)
                sites = [s.domain for s in app.sites.all()]
                
                if provider == 'google':
                    if 'apps.googleusercontent.com' in app.client_id:
                        self.stdout.write(self.style.SUCCESS(f'✅ {provider.title()}: Ready ({app.client_id[:20]}...)'))
                    else:
                        self.stdout.write(self.style.WARNING(f'⚠️  {provider.title()}: Check credentials'))
                elif provider == 'facebook':
                    if app.client_id != 'YOUR_FACEBOOK_APP_ID':
                        self.stdout.write(self.style.SUCCESS(f'✅ {provider.title()}: Ready ({app.client_id})'))
                    else:
                        self.stdout.write(self.style.WARNING(f'⚠️  {provider.title()}: Needs real credentials'))
                elif provider == 'twitter':
                    if app.client_id != 'YOUR_TWITTER_API_KEY':
                        self.stdout.write(self.style.SUCCESS(f'✅ {provider.title()}: Ready ({app.client_id[:20]}...)'))
                    else:
                        self.stdout.write(self.style.WARNING(f'⚠️  {provider.title()}: Needs real credentials'))
                
                if 'localhost:8000' not in sites:
                    self.stdout.write(f'   ⚠️  Not connected to localhost:8000 site')
                else:
                    self.stdout.write(f'   ✅ Connected to {", ".join(sites)}')
                    
            except SocialApp.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'❌ {provider.title()}: Not configured'))
        
        # Check settings
        self.stdout.write('\n⚙️  Settings Check:')
        
        required_settings = [
            ('SITE_ID', settings.SITE_ID),
            ('LOGIN_REDIRECT_URL', settings.LOGIN_REDIRECT_URL),
            ('ACCOUNT_EMAIL_VERIFICATION', getattr(settings, 'ACCOUNT_EMAIL_VERIFICATION', None)),
        ]
        
        for setting_name, setting_value in required_settings:
            if setting_value:
                self.stdout.write(f'   ✅ {setting_name}: {setting_value}')
            else:
                self.stdout.write(f'   ⚠️  {setting_name}: Not set')
        
        # Check middleware
        middleware = settings.MIDDLEWARE
        if 'allauth.account.middleware.AccountMiddleware' in middleware:
            self.stdout.write('   ✅ AccountMiddleware: Configured')
        else:
            self.stdout.write(self.style.ERROR('   ❌ AccountMiddleware: Missing'))
        
        # Test URLs
        self.stdout.write('\n🌐 Test URLs:')
        base_url = 'http://localhost:8000'
        test_urls = [
            f'{base_url}/accounts/login/',
            f'{base_url}/accounts/signup/',
            f'{base_url}/accounts/google/login/',
            f'{base_url}/accounts/facebook/login/',
            f'{base_url}/accounts/twitter/login/',
            f'{base_url}/admin/',
        ]
        
        for url in test_urls:
            self.stdout.write(f'   🔗 {url}')
        
        # Summary
        google_ready = SocialApp.objects.filter(provider='google', client_id__contains='apps.googleusercontent.com').exists()
        facebook_ready = SocialApp.objects.filter(provider='facebook').exclude(client_id='YOUR_FACEBOOK_APP_ID').exists()
        twitter_ready = SocialApp.objects.filter(provider='twitter').exclude(client_id='YOUR_TWITTER_API_KEY').exists()
        
        self.stdout.write('\n' + '='*50)
        self.stdout.write('📊 SUMMARY:')
        self.stdout.write('='*50)
        
        if google_ready:
            self.stdout.write('🟢 Google: Ready for testing')
        else:
            self.stdout.write('🟡 Google: Needs configuration')
            
        if facebook_ready:
            self.stdout.write('🟢 Facebook: Ready for testing')
        else:
            self.stdout.write('🟡 Facebook: Needs real credentials')
            
        if twitter_ready:
            self.stdout.write('🟢 Twitter: Ready for testing')
        else:
            self.stdout.write('🟡 Twitter: Needs real credentials')
        
        ready_count = sum([google_ready, facebook_ready, twitter_ready])
        
        if ready_count == 3:
            self.stdout.write(self.style.SUCCESS('\n🎉 All social providers ready!'))
        elif ready_count >= 1:
            self.stdout.write(self.style.WARNING(f'\n⚡ {ready_count}/3 providers ready'))
        else:
            self.stdout.write(self.style.ERROR('\n🔧 Setup required'))
        
        self.stdout.write(f'\n🚀 Start testing: {base_url}/accounts/login/')
        
        if not facebook_ready or not twitter_ready:
            self.stdout.write('\n📝 To add missing credentials:')
            if not facebook_ready:
                self.stdout.write('   Facebook: python manage.py setup_all_social --facebook-app-id YOUR_ID --facebook-secret YOUR_SECRET')
            if not twitter_ready:
                self.stdout.write('   Twitter: python manage.py setup_all_social --twitter-api-key YOUR_KEY --twitter-secret YOUR_SECRET')
