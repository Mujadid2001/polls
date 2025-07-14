# Social Authentication Setup Guide

This guide will help you configure Google, Facebook, and Twitter authentication for the Polls Django application.

## 🚀 Quick Start

The social authentication is already integrated into the application. You just need to configure the API credentials.

## 📋 Prerequisites

1. Django application is running
2. Admin account created (username: `admin`, password: `admin123`)
3. Internet connection for API setup

## 🔧 Configuration Steps

### 1. Google OAuth2 Setup

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
2. **Create a new project** or select an existing one
3. **Enable Google+ API**:
   - Go to "APIs & Services" → "Library"
   - Search for "Google+ API" and enable it
4. **Create OAuth2 credentials**:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth 2.0 Client IDs"
   - Application type: "Web application"
   - Name: "Polls App"
   - Authorized redirect URIs: `http://localhost:8000/accounts/google/login/callback/`
5. **Copy the Client ID and Client Secret**

### 2. Facebook OAuth2 Setup

1. **Go to Facebook Developers**: https://developers.facebook.com/
2. **Create a new app**:
   - Click "Create App"
   - Choose "Consumer" → "Next"
   - Enter app name: "Polls App"
3. **Add Facebook Login**:
   - In the app dashboard, click "Add Product"
   - Find "Facebook Login" and click "Set Up"
4. **Configure OAuth settings**:
   - Go to Facebook Login → Settings
   - Valid OAuth Redirect URIs: `http://localhost:8000/accounts/facebook/login/callback/`
5. **Get App ID and App Secret**:
   - Go to Settings → Basic
   - Copy App ID and App Secret

### 3. Twitter OAuth Setup

1. **Go to Twitter Developer Portal**: https://developer.twitter.com/
2. **Create a new app**:
   - Apply for a developer account if needed
   - Create a new project/app
3. **Configure OAuth settings**:
   - In app settings, enable "Request email from users"
   - Callback URL: `http://localhost:8000/accounts/twitter/login/callback/`
4. **Get API Keys**:
   - Go to "Keys and tokens"
   - Copy API Key and API Secret Key

## 🔑 Adding Credentials to Django

1. **Access Django Admin**: http://localhost:8000/admin/
2. **Login with**: username: `admin`, password: `admin123`
3. **Go to**: Social Applications → Social applications
4. **Edit each provider**:

### Google:
- Provider: google
- Name: Google OAuth2
- Client id: [Your Google Client ID]
- Secret key: [Your Google Client Secret]
- Sites: Select "localhost:8000"

### Facebook:
- Provider: facebook
- Name: Facebook OAuth2  
- Client id: [Your Facebook App ID]
- Secret key: [Your Facebook App Secret]
- Sites: Select "localhost:8000"

### Twitter:
- Provider: twitter
- Name: Twitter OAuth
- Client id: [Your Twitter API Key]
- Secret key: [Your Twitter API Secret]
- Sites: Select "localhost:8000"

## 🎯 Testing Social Authentication

1. **Start the server**: `python manage.py runserver`
2. **Go to**: http://localhost:8000/accounts/login/
3. **Try social login buttons**:
   - "Continue with Google"
   - "Continue with Facebook" 
   - "Continue with Twitter"

## 🔧 Troubleshooting

### Common Issues:

1. **"Invalid redirect URI"**:
   - Make sure callback URLs match exactly in provider settings
   - For development: `http://localhost:8000/accounts/[provider]/login/callback/`

2. **"App not configured"**:
   - Check that the Social Application is created in Django admin
   - Verify the provider name matches exactly (google, facebook, twitter)

3. **"Invalid client_id"**:
   - Double-check the Client ID/App ID in Django admin
   - Make sure there are no extra spaces

4. **Email permission denied**:
   - For Twitter: Enable "Request email from users" in app settings
   - For Facebook: Make sure app is live or you're added as a test user

## 🌟 Features

- **One-click social login**
- **Automatic account creation**
- **Profile information sync**
- **Multiple social accounts per user**
- **Easy account linking/unlinking**

## 🔒 Security Features

- **Secure OAuth2 flow**
- **CSRF protection**
- **Session management**
- **Rate limiting**
- **Verified email handling**

## 📱 Social Account Management

Users can:
- Connect multiple social accounts
- Disconnect social accounts  
- View connected accounts in profile
- Login with any connected account

Access via: Profile → Social Accounts

## 🎨 UI Features

- **Modern Bootstrap 5 design**
- **Responsive social login buttons**
- **Clear connection status**
- **Intuitive account management**

## 📧 Email Configuration

For production, update `settings.py`:

```python
# Email configuration for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

For development, email verification is optional and emails are logged to console.

## 🚀 Production Setup

For production deployment:

1. **Update allowed hosts** in `settings.py`
2. **Update redirect URIs** in social providers
3. **Enable HTTPS** and update security settings
4. **Configure proper email backend**
5. **Set secure cookie settings**

Example production URLs:
- Google: `https://yoursite.com/accounts/google/login/callback/`
- Facebook: `https://yoursite.com/accounts/facebook/login/callback/`
- Twitter: `https://yoursite.com/accounts/twitter/login/callback/`

## 🎯 Success!

Once configured, users can:
- Register/login with social accounts
- Link multiple social accounts
- Enjoy seamless authentication experience
- Access role-based features based on their account type

The social authentication integrates seamlessly with the existing role-based access control system.
