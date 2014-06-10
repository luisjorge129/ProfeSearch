from os import environ

from django.core.exceptions import ImproperlyConfigured

from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True
TEMPLATE_DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_PATCH_SETTINGS = False


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_setting('SECRET_KEY')
