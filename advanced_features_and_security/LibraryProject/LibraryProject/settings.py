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
    "bookshelf.CustomUser
]

# Set the custom user model to be used by the authentication system
AUTH_USER_MODEL = 'users.CustomUser'
"""
Django settings for LibraryProject project.
"""
# This is a partial file. Add these settings to your existing settings.py.

# Set DEBUG to False in production
DEBUG = False

# Security Enhancements
# These headers provide additional browser-side protections
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Enforce secure cookies, ensuring they are only sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Redirect all non-HTTPS requests to HTTPS
# Note: You may need a reverse proxy (like Nginx) to handle this in a production environment.
# SECURE_SSL_REDIRECT = True # Uncomment in production

# Enable Host header validation to prevent HTTP Host header attacks
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Add django.middleware.csrf.CsrfViewMiddleware to your MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
