from .base import *

ALLOWED_HOSTS = []

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = 'devolpment'
