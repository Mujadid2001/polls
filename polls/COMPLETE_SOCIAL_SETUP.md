# Complete Social Authentication Setup Guide

This guide provides step-by-step instructions for setting up Google, Facebook, and Twitter authentication.

## 🎯 Current Status

✅ **Google OAuth2**: Fully configured and working  
⚠️ **Facebook OAuth2**: Framework ready, needs real credentials  
⚠️ **Twitter OAuth**: Framework ready, needs real credentials  

## 🔧 Quick Test

Visit: http://localhost:8000/accounts/login/

- **Google Login**: Should work immediately
- **Facebook/Twitter**: Will show buttons but need real API keys

## 📋 Step-by-Step Setup

### 1. Facebook OAuth2 Setup

#### Create Facebook App:
1. Go to: https://developers.facebook.com/
2. Click **"Create App"** → **"Consumer"** → **"Next"**
3. App name: **"Polls App"** → **"Create App"**

#### Configure Facebook Login:
1. In app dashboard → **"Add Product"** → **"Facebook Login"** → **"Set Up"**
2. Go to **Facebook Login** → **"Settings"**
3. Add Valid OAuth Redirect URI: `http://localhost:8000/accounts/facebook/login/callback/`
4. Save changes

#### Get Credentials:
1. Go to **"Settings"** → **"Basic"**
2. Copy **App ID** and **App Secret**
3. Add to Django:
```bash
python manage.py setup_all_social --facebook-app-id YOUR_APP_ID --facebook-secret YOUR_APP_SECRET
```

#### Example:
```bash
python manage.py setup_all_social --facebook-app-id 1234567890123456 --facebook-secret abcd1234efgh5678ijkl9012mnop3456
```

### 2. Twitter OAuth Setup

#### Create Twitter App:
1. Go to: https://developer.twitter.com/
2. Apply for developer account (if needed)
3. Create new project/app: **"Polls App"**

#### Configure OAuth:
1. In app settings → **"User authentication settings"**
2. Enable **"OAuth 1.0a"**
3. App permissions: **"Read"** (sufficient for login)
4. Callback URL: `http://localhost:8000/accounts/twitter/login/callback/`
5. Website URL: `http://localhost:8000`

#### Get Credentials:
1. Go to **"Keys and Tokens"**
2. Copy **API Key** and **API Secret Key**
3. Add to Django:
```bash
python manage.py setup_all_social --twitter-api-key YOUR_API_KEY --twitter-secret YOUR_API_SECRET
```

#### Example:
```bash
python manage.py setup_all_social --twitter-api-key AbCdEfGhIjKlMnOpQrSt1234567890 --twitter-secret AbCdEfGhIjKlMnOpQrStUvWxYz1234567890AbCdEfGhIjKlMn
```

## 🚀 Testing Social Login

### Test Google (Ready Now):
1. Go to: http://localhost:8000/accounts/login/
2. Click **"Continue with Google"**
3. Should redirect to Google OAuth
4. After authentication, creates account with User role

### Test Facebook (After Setup):
1. Go to: http://localhost:8000/accounts/login/
2. Click **"Continue with Facebook"**
3. Should redirect to Facebook OAuth
4. After authentication, creates account with User role

### Test Twitter (After Setup):
1. Go to: http://localhost:8000/accounts/login/
2. Click **"Continue with Twitter"**
3. Should redirect to Twitter OAuth
4. After authentication, creates account with User role

## 🔧 Troubleshooting

### Common Issues:

#### "Invalid redirect_uri":
- Check callback URLs match exactly in provider settings
- For development use: `http://localhost:8000/accounts/[provider]/login/callback/`

#### "App not configured":
- Verify Social Application exists in Django Admin
- Check provider name matches exactly (google, facebook, twitter)

#### "Invalid client_id":
- Double-check credentials in Django Admin
- No extra spaces or characters

#### Facebook "App not live":
- Add yourself as test user in Facebook App
- Or make app live in App Review

#### Twitter email permission:
- Enable "Request email from users" in Twitter app settings

## 📱 Current Setup Commands

### View current configuration:
```bash
python manage.py shell -c "
from allauth.socialaccount.models import SocialApp
for app in SocialApp.objects.all():
    print(f'{app.provider}: {app.client_id} (Sites: {[s.domain for s in app.sites.all()]})')
"
```

### Update individual providers:
```bash
# Facebook only
python manage.py setup_all_social --facebook-app-id YOUR_APP_ID --facebook-secret YOUR_SECRET

# Twitter only  
python manage.py setup_all_social --twitter-api-key YOUR_API_KEY --twitter-secret YOUR_SECRET

# All at once
python manage.py setup_all_social --facebook-app-id FB_ID --facebook-secret FB_SECRET --twitter-api-key TW_KEY --twitter-secret TW_SECRET
```

## 🎨 UI Features

The login page includes:
- Modern Bootstrap 5 design
- Responsive social login buttons
- Font Awesome icons
- Clear provider identification
- Error handling and messages

## 🔒 Security Features

- CSRF protection
- Secure OAuth2/OAuth1 flows
- Rate limiting on failed attempts
- Session management
- Email verification options

## 🌟 User Experience

After social login:
- Automatic account creation
- Profile with social info
- Role assignment (User by default)
- Dashboard access based on role
- Ability to link multiple social accounts

## ✅ Success Indicators

When working correctly:
1. Social buttons appear on login page
2. Clicking redirects to provider
3. After auth, redirects back to app
4. User account created automatically
5. User logged in and redirected to dashboard

## 🎯 Next Steps

1. **Test Google login** (should work now)
2. **Set up Facebook app** and add credentials
3. **Set up Twitter app** and add credentials
4. **Test all providers**
5. **Configure for production** when ready

The social authentication system is now fully integrated and ready for use!
