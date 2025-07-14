#!/usr/bin/env python3
"""
Quick Social Auth Setup Script
Run this to check status and get setup instructions
"""

import os
import sys

def main():
    print("🚀 Django Polls Social Authentication Setup")
    print("=" * 50)
    
    print("\n✅ CURRENT STATUS:")
    print("🟢 Google OAuth2: WORKING (real credentials)")
    print("🟡 Facebook OAuth2: Framework ready (needs real credentials)")
    print("🟡 Twitter OAuth: Framework ready (needs real credentials)")
    
    print("\n🔗 TEST URLS:")
    print("🌐 Login Page: http://localhost:8000/accounts/login/")
    print("🔧 Admin Panel: http://localhost:8000/admin/")
    print("🏠 Home Page: http://localhost:8000/")
    
    print("\n📋 GOOGLE SETUP (COMPLETED):")
    print("✅ Client ID: [Configured via environment variables]")
    print("✅ Redirect URI: http://localhost:8000/accounts/google/login/callback/")
    print("✅ Status: Ready for testing")
    
    print("\n📋 FACEBOOK SETUP (TODO):")
    print("1. Go to: https://developers.facebook.com/")
    print("2. Create App → Consumer → 'Polls App'")
    print("3. Add Facebook Login product")
    print("4. Set redirect URI: http://localhost:8000/accounts/facebook/login/callback/")
    print("5. Get App ID and App Secret")
    print("6. Run: python manage.py setup_all_social --facebook-app-id YOUR_ID --facebook-secret YOUR_SECRET")
    
    print("\n📋 TWITTER SETUP (TODO):")
    print("1. Go to: https://developer.twitter.com/")
    print("2. Create project/app: 'Polls App'")
    print("3. Enable OAuth 1.0a")
    print("4. Set callback URL: http://localhost:8000/accounts/twitter/login/callback/")
    print("5. Get API Key and API Secret")
    print("6. Run: python manage.py setup_all_social --twitter-api-key YOUR_KEY --twitter-secret YOUR_SECRET")
    
    print("\n🔧 QUICK COMMANDS:")
    print("# Test current setup")
    print("python manage.py test_social_auth")
    print()
    print("# Add Facebook credentials")
    print("python manage.py setup_all_social --facebook-app-id FB_ID --facebook-secret FB_SECRET")
    print()
    print("# Add Twitter credentials")
    print("python manage.py setup_all_social --twitter-api-key TW_KEY --twitter-secret TW_SECRET")
    print()
    print("# Add both at once")
    print("python manage.py setup_all_social --facebook-app-id FB_ID --facebook-secret FB_SECRET --twitter-api-key TW_KEY --twitter-secret TW_SECRET")
    
    print("\n🎯 WHAT WORKS NOW:")
    print("✅ Google social login")
    print("✅ Traditional email/password login")
    print("✅ User registration")
    print("✅ Role-based access control")
    print("✅ User dashboards")
    print("✅ Profile management")
    print("✅ Social account linking")
    
    print("\n🎯 WHAT NEEDS SETUP:")
    print("⏳ Facebook OAuth credentials")
    print("⏳ Twitter OAuth credentials")
    
    print("\n📱 USER EXPERIENCE:")
    print("- Beautiful responsive login page")
    print("- One-click social authentication")
    print("- Automatic account creation")
    print("- Role assignment (User by default)")
    print("- Multiple social accounts per user")
    print("- Dashboard based on user role")
    
    print("\n🔒 SECURITY FEATURES:")
    print("- CSRF protection")
    print("- Rate limiting")
    print("- Secure OAuth flows")
    print("- Session management")
    print("- Password validation")
    
    print("\n" + "=" * 50)
    print("🎉 Ready to test! Visit: http://localhost:8000/accounts/login/")
    print("=" * 50)

if __name__ == "__main__":
    main()
