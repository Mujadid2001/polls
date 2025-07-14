# PowerShell script to securely set up Google OAuth credentials
# Run this script to set environment variables for your session

Write-Host "🔐 Google OAuth2 Environment Setup" -ForegroundColor Green
Write-Host "=" * 40

# TODO: Replace these with your actual Google OAuth credentials
$GoogleClientId = "YOUR_GOOGLE_CLIENT_ID_HERE"
$GoogleClientSecret = "YOUR_GOOGLE_CLIENT_SECRET_HERE"

# Check if credentials are set
if ($GoogleClientId -eq "YOUR_GOOGLE_CLIENT_ID_HERE" -or $GoogleClientSecret -eq "YOUR_GOOGLE_CLIENT_SECRET_HERE") {
    Write-Host "❌ Please update this script with your Google OAuth credentials!" -ForegroundColor Red
    Write-Host "📋 Edit setup_google_env.ps1 and replace:" -ForegroundColor Yellow
    Write-Host "   YOUR_GOOGLE_CLIENT_ID_HERE with your actual Client ID" -ForegroundColor White
    Write-Host "   YOUR_GOOGLE_CLIENT_SECRET_HERE with your actual Client Secret" -ForegroundColor White
    Write-Host ""
    Write-Host "🔗 Get credentials from: https://console.developers.google.com/" -ForegroundColor Cyan
    exit 1
}

Write-Host "Setting environment variables for current session..." -ForegroundColor Yellow

# Set environment variables for current session
$env:GOOGLE_CLIENT_ID = $GoogleClientId
$env:GOOGLE_CLIENT_SECRET = $GoogleClientSecret

Write-Host "✅ Environment variables set!" -ForegroundColor Green
Write-Host "📋 Variables set:"
Write-Host "   GOOGLE_CLIENT_ID: $($GoogleClientId.Substring(0,[Math]::Min(20, $GoogleClientId.Length)))..." -ForegroundColor Cyan
Write-Host "   GOOGLE_CLIENT_SECRET: $($GoogleClientSecret.Substring(0,[Math]::Min(10, $GoogleClientSecret.Length)))..." -ForegroundColor Cyan

Write-Host "`n🚀 Now you can run:" -ForegroundColor Green
Write-Host "   python manage.py setup_google_oauth" -ForegroundColor White
Write-Host "   python secure_social_setup.py" -ForegroundColor White

Write-Host "`n⚠️  Note: These variables are only set for this PowerShell session." -ForegroundColor Yellow
Write-Host "   To set them permanently, use:" -ForegroundColor Yellow
Write-Host "   setx GOOGLE_CLIENT_ID `"$GoogleClientId`"" -ForegroundColor White
Write-Host "   setx GOOGLE_CLIENT_SECRET `"$GoogleClientSecret`"" -ForegroundColor White
