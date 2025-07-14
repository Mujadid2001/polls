from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm, AdminUserRoleForm
from .models import UserProfile, UserRole

def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home_polls:home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home_polls:home')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                next_page = request.GET.get('next', 'home_polls:home')
                return redirect(next_page)
        messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    """User logout view"""
    username = request.user.username
    logout(request)
    messages.success(request, f'You have been logged out successfully, {username}!')
    return redirect('home_polls:home')

@login_required
def profile_view(request):
    """User profile view"""
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    """Edit user profile view"""
    profile = request.user.profile
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'accounts/profile_edit.html', {'form': form})

def is_admin(user):
    """Check if user is admin"""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.is_admin()

def is_moderator_or_admin(user):
    """Check if user is moderator or admin"""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.can_moderate_content()

@user_passes_test(is_admin)
def admin_users_view(request):
    """Admin view to manage users"""
    search_query = request.GET.get('search', '')
    role_filter = request.GET.get('role', '')
    
    users = User.objects.select_related('profile').all()
    
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    if role_filter:
        users = users.filter(profile__role=role_filter)
    
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'role_filter': role_filter,
        'role_choices': UserRole.choices,
    }
    
    return render(request, 'accounts/admin_users.html', context)

@user_passes_test(is_admin)
def admin_user_edit_view(request, user_id):
    """Admin view to edit user roles"""
    user = get_object_or_404(User, id=user_id)
    profile = user.profile
    
    if request.method == 'POST':
        form = AdminUserRoleForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'User {user.username} has been updated successfully!')
            return redirect('accounts:admin_users')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AdminUserRoleForm(instance=profile)
    
    return render(request, 'accounts/admin_user_edit.html', {
        'form': form,
        'user': user,
        'profile': profile
    })

@login_required
def dashboard_view(request):
    """User dashboard based on role"""
    user = request.user
    profile = user.profile
    
    context = {
        'user': user,
        'profile': profile,
    }
    
    if profile.is_admin():
        # Admin dashboard with statistics
        total_users = User.objects.count()
        total_admins = UserProfile.objects.filter(role=UserRole.ADMIN).count()
        total_moderators = UserProfile.objects.filter(role=UserRole.MODERATOR).count()
        total_regular_users = UserProfile.objects.filter(role=UserRole.USER).count()
        recent_users = User.objects.select_related('profile').order_by('-date_joined')[:5]
        
        context.update({
            'total_users': total_users,
            'total_admins': total_admins,
            'total_moderators': total_moderators,
            'total_regular_users': total_regular_users,
            'recent_users': recent_users,
        })
        return render(request, 'accounts/admin_dashboard.html', context)
    
    elif profile.is_moderator():
        # Moderator dashboard
        from home_polls.models import Question
        recent_questions = Question.objects.order_by('-pub_date')[:10]
        context.update({
            'recent_questions': recent_questions,
        })
        return render(request, 'accounts/moderator_dashboard.html', context)
    
    else:
        # Regular user dashboard
        from home_polls.models import Question
        latest_questions = Question.objects.order_by('-pub_date')[:5]
        context.update({
            'latest_questions': latest_questions,
        })
        return render(request, 'accounts/user_dashboard.html', context)
