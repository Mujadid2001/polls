# Django Polls App with Authentication & Social Login

A complete Django polling application with user authentication, role-based access control, and social media login integration.

## 🚀 Features

### Core Features
- **Interactive Polling System**: Create, vote on, and view poll results
- **User Authentication**: Complete registration/login system
- **Role-Based Access Control**: Admin, Moderator, and User roles
- **Social Authentication**: Login with Google, Facebook, or Twitter
- **Responsive Design**: Bootstrap 5 with modern UI

### Authentication Features
- Traditional email/password registration and login
- Social media authentication (Google, Facebook, Twitter)
- User profile management
- Role-based dashboards and permissions
- Account linking/unlinking for social accounts

## 🔧 Quick Start

1. **Install dependencies**:
   ```bash
   pip install django django-allauth PyJWT cryptography
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the application**: http://localhost:8000

## 🔑 Social Authentication Setup

For social login functionality, see the detailed setup guide: [SOCIAL_AUTH_SETUP.md](polls/SOCIAL_AUTH_SETUP.md)

### Quick Social Auth Setup:
1. Configure OAuth apps in Google, Facebook, Twitter
2. Add credentials in Django Admin → Social Applications
3. Test social login at http://localhost:8000/accounts/login/

## 👥 User Roles

- **Admin**: Full system access, user management, all polls
- **Moderator**: Poll management, moderate content
- **User**: Vote on polls, view results, manage own profile

## 📱 Application Structure

```
polls/
├── home_polls/          # Main polls application
├── accounts/            # Authentication system
├── polls/              # Django project settings
└── SOCIAL_AUTH_SETUP.md # Social authentication guide
```

## 🎯 Default Admin Account

- **Username**: admin
- **Password**: admin123
- **Role**: Admin (full access)

## 🌟 Technology Stack

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (development)
- **Authentication**: django-allauth
- **Social OAuth**: Google, Facebook, Twitter APIs
