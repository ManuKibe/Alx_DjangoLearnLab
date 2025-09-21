INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
    INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # enables token-based auth
    'api',  # your app
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # default: require auth
    ],
}

]
