from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Administrator'
    MODERATOR = 'moderator', 'Moderator'
    USER = 'user', 'Regular User'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER,
        help_text="User role for access control"
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    def is_admin(self):
        """Check if user has admin role"""
        return self.role == UserRole.ADMIN

    def is_moderator(self):
        """Check if user has moderator role"""
        return self.role == UserRole.MODERATOR

    def is_regular_user(self):
        """Check if user has regular user role"""
        return self.role == UserRole.USER

    def can_create_polls(self):
        """Check if user can create polls"""
        return self.role in [UserRole.ADMIN, UserRole.MODERATOR]

    def can_delete_polls(self):
        """Check if user can delete polls"""
        return self.role == UserRole.ADMIN

    def can_moderate_content(self):
        """Check if user can moderate content"""
        return self.role in [UserRole.ADMIN, UserRole.MODERATOR]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a user profile when a new user is created"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the user profile when the user is saved"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
