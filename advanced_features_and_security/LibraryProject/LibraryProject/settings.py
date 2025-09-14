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
