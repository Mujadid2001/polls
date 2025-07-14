from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

class Command(BaseCommand):
    help = 'Set up social applications for development'

    def handle(self, *args, **options):
        # Get or create the site
        site, created = Site.objects.get_or_create(
            pk=1,
            defaults={
                'domain': 'localhost:8000',
                'name': 'Polls Development Site'
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created site: {site.domain}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Site already exists: {site.domain}')
            )

        # Create placeholder social apps
        providers = [
            {
                'provider': 'google',
                'name': 'Google OAuth2',
                'client_id': 'your-google-client-id',
                'secret': 'your-google-client-secret',
            },
            {
                'provider': 'facebook',
                'name': 'Facebook OAuth2',
                'client_id': 'your-facebook-app-id',
                'secret': 'your-facebook-app-secret',
            },
            {
                'provider': 'twitter',
                'name': 'Twitter OAuth',
                'client_id': 'your-twitter-api-key',
                'secret': 'your-twitter-api-secret',
            }
        ]

        for provider_data in providers:
            app, created = SocialApp.objects.get_or_create(
                provider=provider_data['provider'],
                defaults={
                    'name': provider_data['name'],
                    'client_id': provider_data['client_id'],
                    'secret': provider_data['secret'],
                }
            )
            
            if created:
                app.sites.add(site)
                self.stdout.write(
                    self.style.SUCCESS(f'Created {provider_data["name"]} app')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'{provider_data["name"]} app already exists')
                )

        self.stdout.write(
            self.style.SUCCESS('\nSocial applications setup complete!')
        )
        self.stdout.write(
            self.style.WARNING('\nIMPORTANT: You need to update the client IDs and secrets with real values from:')
        )
        self.stdout.write('- Google: https://console.developers.google.com/')
        self.stdout.write('- Facebook: https://developers.facebook.com/')
        self.stdout.write('- Twitter: https://developer.twitter.com/')
        self.stdout.write('\nGo to Django Admin -> Social Applications to update the credentials.')
