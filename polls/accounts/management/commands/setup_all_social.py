from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Set up all social OAuth providers (Google, Facebook, Twitter)'

    def add_arguments(self, parser):
        parser.add_argument('--google-client-id', type=str, help='Google OAuth2 Client ID')
        parser.add_argument('--google-secret', type=str, help='Google OAuth2 Client Secret')
        parser.add_argument('--facebook-app-id', type=str, help='Facebook App ID')
        parser.add_argument('--facebook-secret', type=str, help='Facebook App Secret')
        parser.add_argument('--twitter-api-key', type=str, help='Twitter API Key')
        parser.add_argument('--twitter-secret', type=str, help='Twitter API Secret Key')

    def handle(self, *args, **options):
        # Get the default site
        site = Site.objects.get(pk=1)
        
        # Update site domain for development
        if site.domain == 'example.com':
            site.domain = 'localhost:8000'
            site.name = 'Polls App Development'
            site.save()
            self.stdout.write(self.style.SUCCESS(f'✅ Updated site domain to: {site.domain}'))

        # Google OAuth2 Setup
        google_client_id = options.get('google_client_id') or 'YOUR_GOOGLE_CLIENT_ID'
        google_secret = options.get('google_secret') or 'YOUR_GOOGLE_CLIENT_SECRET'
        
        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            defaults={
                'name': 'Google OAuth2',
                'client_id': google_client_id,
                'secret': google_secret,
            }
        )
        
        if not created:
            google_app.client_id = google_client_id
            google_app.secret = google_secret
            google_app.save()
        
        google_app.sites.add(site)
        self.stdout.write(self.style.SUCCESS('✅ Google OAuth2 configured'))
        
        # Facebook OAuth2 Setup (with demo credentials)
        facebook_app_id = options.get('facebook_app_id') or 'YOUR_FACEBOOK_APP_ID'
        facebook_secret = options.get('facebook_secret') or 'YOUR_FACEBOOK_APP_SECRET'
        
        facebook_app, created = SocialApp.objects.get_or_create(
            provider='facebook',
            defaults={
                'name': 'Facebook OAuth2',
                'client_id': facebook_app_id,
                'secret': facebook_secret,
            }
        )
        
        if not created:
            facebook_app.client_id = facebook_app_id
            facebook_app.secret = facebook_secret
            facebook_app.save()
        
        facebook_app.sites.add(site)
        
        if facebook_app_id == 'YOUR_FACEBOOK_APP_ID':
            self.stdout.write(self.style.WARNING('⚠️  Facebook OAuth2 configured with demo credentials'))
            self.stdout.write('   Please update with real Facebook App ID and Secret')
        else:
            self.stdout.write(self.style.SUCCESS('✅ Facebook OAuth2 configured'))
        
        # Twitter OAuth Setup (with demo credentials)
        twitter_api_key = options.get('twitter_api_key') or 'YOUR_TWITTER_API_KEY'
        twitter_secret = options.get('twitter_secret') or 'YOUR_TWITTER_API_SECRET'
        
        twitter_app, created = SocialApp.objects.get_or_create(
            provider='twitter',
            defaults={
                'name': 'Twitter OAuth',
                'client_id': twitter_api_key,
                'secret': twitter_secret,
            }
        )
        
        if not created:
            twitter_app.client_id = twitter_api_key
            twitter_app.secret = twitter_secret
            twitter_app.save()
        
        twitter_app.sites.add(site)
        
        if twitter_api_key == 'YOUR_TWITTER_API_KEY':
            self.stdout.write(self.style.WARNING('⚠️  Twitter OAuth configured with demo credentials'))
            self.stdout.write('   Please update with real Twitter API Key and Secret')
        else:
            self.stdout.write(self.style.SUCCESS('✅ Twitter OAuth configured'))
        
        # Summary
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.SUCCESS('🚀 SOCIAL AUTHENTICATION SETUP COMPLETE!'))
        self.stdout.write('='*60)
        
        self.stdout.write(f'📍 Site: {site.domain}')
        self.stdout.write(f'🌐 Login URL: http://localhost:8000/accounts/login/')
        self.stdout.write(f'🔧 Admin URL: http://localhost:8000/admin/')
        
        self.stdout.write('\n📋 Configured Providers:')
        self.stdout.write(f'  ✅ Google: {google_app.client_id}')
        self.stdout.write(f'  {"✅" if facebook_app_id != "YOUR_FACEBOOK_APP_ID" else "⚠️ "} Facebook: {facebook_app.client_id}')
        self.stdout.write(f'  {"✅" if twitter_api_key != "YOUR_TWITTER_API_KEY" else "⚠️ "} Twitter: {twitter_app.client_id}')
        
        if facebook_app_id == 'YOUR_FACEBOOK_APP_ID' or twitter_api_key == 'YOUR_TWITTER_API_KEY':
            self.stdout.write('\n📝 To add real credentials:')
            self.stdout.write('  python manage.py setup_all_social --facebook-app-id YOUR_APP_ID --facebook-secret YOUR_SECRET')
            self.stdout.write('  python manage.py setup_all_social --twitter-api-key YOUR_API_KEY --twitter-secret YOUR_SECRET')
        
        self.stdout.write('\n🎯 Next Steps:')
        self.stdout.write('  1. Visit http://localhost:8000/accounts/login/')
        self.stdout.write('  2. Test Google login (working)')
        self.stdout.write('  3. Add real Facebook/Twitter credentials when ready')
        self.stdout.write('  4. Update redirect URIs in provider dashboards:')
        self.stdout.write('     - Google: http://localhost:8000/accounts/google/login/callback/')
        self.stdout.write('     - Facebook: http://localhost:8000/accounts/facebook/login/callback/')
        self.stdout.write('     - Twitter: http://localhost:8000/accounts/twitter/login/callback/')
