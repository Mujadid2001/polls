# 🚀 Setting Up Google OAuth Credentials

This guide shows you how to securely configure Google OAuth for your Django Polls app.

## 🔐 Security First

This project uses **environment variables** to keep your OAuth credentials secure and prevent them from being committed to version control.

## 📋 Quick Setup Steps

### 1. Set Environment Variables (Windows PowerShell)

```powershell
# Set for current session
$env:GOOGLE_CLIENT_ID='YOUR_CLIENT_ID_HERE'
$env:GOOGLE_CLIENT_SECRET='YOUR_CLIENT_SECRET_HERE'

# Or set permanently
setx GOOGLE_CLIENT_ID 'YOUR_CLIENT_ID_HERE'
setx GOOGLE_CLIENT_SECRET 'YOUR_CLIENT_SECRET_HERE'
```

### 2. Run Setup Command

```bash
python manage.py setup_google_oauth
```

### 3. Test the Setup

Visit: http://localhost:8000/accounts/login/

## 🔧 Alternative Setup Methods

### Method 1: Use PowerShell Script

1. Edit `setup_google_env.ps1`
2. Replace placeholder values with your credentials
3. Run: `.\setup_google_env.ps1`
4. Run: `python manage.py setup_google_oauth`

### Method 2: Use Django Command Arguments

```bash
python manage.py setup_all_social \
  --google-client-id YOUR_CLIENT_ID \
  --google-secret YOUR_CLIENT_SECRET
```

### Method 3: Interactive Setup

```bash
python secure_social_setup.py
```

## 🌐 Getting Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.developers.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 Client ID credentials
5. Set authorized redirect URI: `http://localhost:8000/accounts/google/login/callback/`
6. Copy Client ID and Client Secret

## ✅ Verification

Check if everything is working:

```bash
# Test the setup
python manage.py test_social_auth

# Check status
python social_auth_status.py
```

## 🔒 Security Notes

- ✅ Credentials are stored in environment variables
- ✅ No secrets committed to version control  
- ✅ GitHub push protection compatible
- ✅ Production-ready approach

## 🎯 Your Credentials

You have provided the following Google OAuth credentials:
- Client ID: `[Your provided Client ID - configure via environment variables]`
- Client Secret: `[Your provided Client Secret - configure via environment variables]`

> **Important**: Use the environment variable setup methods above to configure these securely.

## 🚨 Troubleshooting

### "Credentials not found" error
- Make sure environment variables are set in current session
- Check spelling of variable names
- Restart terminal/PowerShell after setting permanent variables

### GitHub push rejected
- Remove any hardcoded credentials from code files
- Use environment variables or command arguments instead
- Check `.gitignore` includes credential files

### OAuth redirect error  
- Verify redirect URI in Google Console matches exactly
- Use `http://localhost:8000/accounts/google/login/callback/`

## 🎉 Success!

Once configured, users can:
- Login with Google account
- Automatic account creation
- Role-based dashboard access
- Social account management
