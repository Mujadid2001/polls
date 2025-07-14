from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Admin URLs
    path('admin/users/', views.admin_users_view, name='admin_users'),
    path('admin/users/<int:user_id>/edit/', views.admin_user_edit_view, name='admin_user_edit'),
]
