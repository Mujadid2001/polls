from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    """
    Decorator to check if user has the required role.
    
    Usage:
    @role_required(['admin', 'moderator'])
    def my_view(request):
        pass
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if not hasattr(request.user, 'profile'):
                messages.error(request, 'Access denied: No user profile found.')
                return redirect('home_polls:home')
            
            user_role = request.user.profile.role
            if user_role not in allowed_roles:
                messages.error(request, f'Access denied: {request.user.profile.get_role_display()} role is not authorized for this action.')
                return redirect('home_polls:home')
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def admin_required(view_func):
    """Decorator to require admin role"""
    return role_required(['admin'])(view_func)

def moderator_or_admin_required(view_func):
    """Decorator to require moderator or admin role"""
    return role_required(['admin', 'moderator'])(view_func)

def can_create_polls(view_func):
    """Decorator to check if user can create polls"""
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'profile') or not request.user.profile.can_create_polls():
            messages.error(request, 'Access denied: You do not have permission to create polls.')
            return redirect('home_polls:home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def can_delete_polls(view_func):
    """Decorator to check if user can delete polls"""
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'profile') or not request.user.profile.can_delete_polls():
            messages.error(request, 'Access denied: You do not have permission to delete polls.')
            return redirect('home_polls:home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def can_moderate_content(view_func):
    """Decorator to check if user can moderate content"""
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'profile') or not request.user.profile.can_moderate_content():
            messages.error(request, 'Access denied: You do not have permission to moderate content.')
            return redirect('home_polls:home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
