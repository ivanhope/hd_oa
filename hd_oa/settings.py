"""
Django settings for hd_oa project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i@q%c&)god)@!4noqwy8*mr31)fua$xuphbvv35pflb^8v0r^3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_python3_ldap',
    'admin_confirm',
    'asset',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hd_oa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hd_oa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hd_oa',
	    'USER': 'root',
	    'PASSWORD': 'Hdyw@2021',
	    'HOST': '127.0.0.1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static"),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LDAP
AUTHENTICATION_BACKENDS = [
    # 'django_auth_ldap.backend.LDAPBackend',
    'django_python3_ldap.auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LDAP_AUTH_URL = "ldap://192.168.9.251:389"
LDAP_AUTH_USE_TLS = False
LDAP_AUTH_SEARCH_BASE = 'ou=Users,ou=npnets,dc=npnets,dc=cn'
LDAP_AUTH_OBJECT_CLASS = "user"
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
# sync_user_relations????????????????????????????????????
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
LDAP_AUTH_FORMAT_SEARCH_FILTERS =  "django_python3_ldap.utils.format_search_filters"
LDAP_AUTH_FORMAT_USERNAME =  "django_python3_ldap.utils.format_username_active_directory_principal"
LDAP_AUTH_CONNECTION_USERNAME = "ad-acount" #???????????????????????????
LDAP_AUTH_CONNECTION_PASSWORD = "0d^7^UPqj0" #???????????????????????????
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "npnets.cn"
LDAP_AUTH_CONNECT_TIMEOUT = None
LDAP_AUTH_RECEIVE_TIMEOUT = None



