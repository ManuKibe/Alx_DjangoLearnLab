# This is a partial settings file. You should add this line to your project's main settings.py.

# Add the 'users' app to your INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your custom apps here
    'users',
]

# Set the custom user model to be used by the authentication system
AUTH_USER_MODEL = 'users.CustomUser'
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-secret-for-dev")

# Never run production with DEBUG=True
DEBUG = False  

ALLOWED_HOSTS = ["yourdomain.com", "127.0.0.1", "localhost"]

# Security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True

# Force cookies over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# HSTS (forces HTTPS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# CSP via django-csp if installed
# MIDDLEWARE += ["csp.middleware.CSPMiddleware"]
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "cdnjs.cloudflare.com")  # allow trusted CDNs
CSP_STYLE_SRC = ("'self'", "fonts.googleapis.com", "cdnjs.cloudflare.com")
CSP_FONT_SRC = ("'self'", "fonts.gstatic.com")
