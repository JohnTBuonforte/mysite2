"""
Django settings for mysite2 project.

Generated by 'django-admin startproject' using Django .

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.7/ref/settings/#secret-key
#
# We should consider storing the secret key outside of the source code.
# You can permanently set an environment variable values on Heroku.
#  See: https://devcenter.heroku.com/articles/config-vars
#
#  heroku config:set DJANGO_SECRET_KEY='dwoh)p(k)7_c*+$9!b0ib%qyk8zddipmg*$g(hpv-v=x+g*rcg'
# 
# and then read the secret key from the environment variable with:
#  SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
#
SECRET_KEY = 'dwoh)p(k)7_c*+$9!b0ib%qyk8zddipmg*$g(hpv-v=x+g*rcg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite2.urls'

# WSGI configuration
# See https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
WSGI_APPLICATION = 'mysite2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Parse database configuration from DATABASE_URL using dj-database-url
# if the environment variable is not defined then default to mysite2_db.sqlite3.
# https://github.com/kennethreitz/dj-database-url
#
# The production environment on Heroku already defines DATABASE_URL.
#
# In your local test and development virtual environment you can use the following
# PowerShell statement:
#  $Env:DATABASE_URL="postgres://USER:PASSWORD@usmasvddsol.eecs.usma.edu:5432/DATABASE"
# replace USER, PASSWORD, and DATABASE with the values mentioned in class.
#
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(default="sqlite:///"+os.path.join(BASE_DIR, 'mysite2_db.sqlite3')),
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static asset configuration for static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# dj-static configuration
# See: https://github.com/kennethreitz/dj-static
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Output Django logs to Heroku logplex
# Django logging: https://docs.djangoproject.com/en/1.7/topics/logging/
# Heroku logging: https://devcenter.heroku.com/articles/logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        }
    }
}
