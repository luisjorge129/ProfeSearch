from .base import *

ALLOWED_HOSTS = []

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_PATCH_SETTINGS = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = 'development'

# Application definition
INSTALLED_APPS += (
    'django_extensions',
)
