#!/usr/bin/env python3
"""
Secure Social Auth Setup Script
Uses environment variables for OAuth credentials
"""

import os
import sys
import subprocess

def setup_google_oauth():
    """Setup Google OAuth with environment variables"""
    print("🔐 Setting up Google OAuth2...")
    
    # Check if credentials are already in environment
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        print("❌ Google OAuth2 credentials not found in environment variables!")
        print("\n📋 To set up Google OAuth2:")
        print("1. Set environment variables (Windows PowerShell):")
        print("   $env:GOOGLE_CLIENT_ID='your_client_id_here'")
        print("   $env:GOOGLE_CLIENT_SECRET='your_client_secret_here'")
        print()
        print("2. Or set them permanently:")
        print("   setx GOOGLE_CLIENT_ID 'your_client_id_here'")
        print("   setx GOOGLE_CLIENT_SECRET 'your_client_secret_here'")
        print()
        print("3. Then run this script again")
        return False
    
    # Run the Django management command
    try:
        result = subprocess.run([
            sys.executable, 'manage.py', 'setup_google_oauth'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Google OAuth2 setup successful!")
            print(result.stdout)
            return True
        else:
            print("❌ Google OAuth2 setup failed!")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error running setup command: {e}")
        return False

def setup_social_providers():
    """Setup all social providers with command line arguments"""
    print("🔧 Social Provider Setup Options:")
    print()
    print("Option 1: Use environment variables (recommended for Google)")
    print("Option 2: Use command line arguments (for Facebook/Twitter)")
    print()
    
    choice = input("Choose option (1 or 2): ").strip()
    
    if choice == "1":
        return setup_google_oauth()
    elif choice == "2":
        print("\n📋 Command line setup:")
        print("# For Google:")
        print("python manage.py setup_all_social --google-client-id YOUR_ID --google-secret YOUR_SECRET")
        print()
        print("# For Facebook:")
        print("python manage.py setup_all_social --facebook-app-id YOUR_ID --facebook-secret YOUR_SECRET")
        print()
        print("# For Twitter:")
        print("python manage.py setup_all_social --twitter-api-key YOUR_KEY --twitter-secret YOUR_SECRET")
        print()
        print("# For all at once:")
        print("python manage.py setup_all_social --google-client-id G_ID --google-secret G_SECRET --facebook-app-id FB_ID --facebook-secret FB_SECRET --twitter-api-key TW_KEY --twitter-secret TW_SECRET")
        return False
    else:
        print("❌ Invalid choice")
        return False

def main():
    print("🚀 Secure Django Social Authentication Setup")
    print("=" * 50)
    
    # Check if Django is available
    try:
        import django
        print(f"✅ Django {django.get_version()} found")
    except ImportError:
        print("❌ Django not found! Please install Django first.")
        return
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ manage.py not found! Please run this script from the Django project directory.")
        return
    
    print("\n🔐 SECURE SETUP METHODS:")
    print("This script helps you set up social authentication securely.")
    print("We'll use environment variables to avoid hardcoding credentials.")
    
    if not setup_social_providers():
        print("\n📚 SECURITY BEST PRACTICES:")
        print("- Never commit OAuth credentials to version control")
        print("- Use environment variables for sensitive data")
        print("- Use .env files for local development")
        print("- Use proper secret management in production")
    
    print("\n🔗 Quick Links:")
    print("📖 Setup Guide: COMPLETE_SOCIAL_SETUP.md")
    print("🌐 Test Login: http://localhost:8000/accounts/login/")
    print("🔧 Admin Panel: http://localhost:8000/admin/")

if __name__ == "__main__":
    main()
