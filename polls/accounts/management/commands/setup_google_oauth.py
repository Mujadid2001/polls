from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Set up Google OAuth2 credentials'

    def handle(self, *args, **options):
        # Get the default site
        site = Site.objects.get(pk=1)
        
        # Get credentials from environment variables
        import os
        client_id = os.getenv('GOOGLE_CLIENT_ID', 'YOUR_GOOGLE_CLIENT_ID')
        client_secret = os.getenv('GOOGLE_CLIENT_SECRET', 'YOUR_GOOGLE_CLIENT_SECRET')
        
        if client_id == 'YOUR_GOOGLE_CLIENT_ID' or client_secret == 'YOUR_GOOGLE_CLIENT_SECRET':
            self.stdout.write(self.style.ERROR('❌ Google OAuth2 credentials not found!'))
            self.stdout.write('Please set environment variables:')
            self.stdout.write('  GOOGLE_CLIENT_ID=your_client_id')
            self.stdout.write('  GOOGLE_CLIENT_SECRET=your_client_secret')
            return
        
        # Create or update Google social app
        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            defaults={
                'name': 'Google OAuth2',
                'client_id': client_id,
                'secret': client_secret,
            }
        )
        
        if not created:
            # Update existing app
            google_app.client_id = client_id
            google_app.secret = client_secret
            google_app.save()
            self.stdout.write(self.style.SUCCESS('Updated existing Google OAuth2 app'))
        else:
            self.stdout.write(self.style.SUCCESS('Created new Google OAuth2 app'))
        
        # Add the site to the social app
        google_app.sites.add(site)
        
        self.stdout.write(self.style.SUCCESS('✅ Google OAuth2 setup completed!'))
        self.stdout.write(f'Client ID: {google_app.client_id}')
        self.stdout.write(f'Site: {site.domain}')
        self.stdout.write('🚀 You can now test Google login at: http://localhost:8000/accounts/login/')
