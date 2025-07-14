from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile, UserRole

class Command(BaseCommand):
    help = 'Create initial admin user with admin role'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Admin username', default='admin')
        parser.add_argument('--email', type=str, help='Admin email', default='admin@example.com')
        parser.add_argument('--password', type=str, help='Admin password', default='admin123')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" already exists.')
            )
            return

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name='System',
            last_name='Administrator',
            is_staff=True,
            is_superuser=True
        )

        # Update profile to admin role
        profile = user.profile
        profile.role = UserRole.ADMIN
        profile.is_verified = True
        profile.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created admin user "{username}" with password "{password}"'
            )
        )
