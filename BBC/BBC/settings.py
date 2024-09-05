"""
Django settings for BBC project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2sx8fo7!2xrglvuoxcs7c5ump5g#sw*r)9y&v))yw%0czc2frs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

SITE_ID = 1

SITE_URL = 'http://127.0.0.1:8000'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'BBC.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'BBC.wsgi.application'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

LOGIN_REDIRECT_URL = '/news'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "kolchinaleksandr2432@yandex.ru"
EMAIL_HOST_PASSWORD = "vrzqjbvxycylvliv"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = 'Внимание!'

DEFAULT_FROM_EMAIL = "kolchinaleksandr2432@yandex.ru"

SERVER_EMAIL = "kolchinaleksandr2432@yandex.ru"
MANAGERS = (
    ('Aleksandr', 'alexander_2424@mail.ru'),
)
ADMINS = (
    ('Polina', 'polinakolchina98@mail.ru'),
)

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}




# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'style': '{',
#     'formatters': {
#         'debug_form': {
#             'format': '%(asctime)s %(levelname)s %(message)s'
#         },
#         'warning_form': {
#             'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
#         },
#         'error_form': {
#             'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
#         },
#         'general_form': {
#             'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
#         },
#     },
#
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'formatter': 'debug_form',
#             'class': 'logging.StreamHandler',
#         },
#
#         'console_warning': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'warning_form',
#         },
#
#         'console_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'error_form',
#         },
#
#         'general_log': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'formatter': 'general_form',
#             'filename': os.path.join(BASE_DIR, 'general.log'),
#         },
#
#         'errors_log': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'formatter': 'error_form',
#             'filename': os.path.join(BASE_DIR, 'errors.log'),
#         },
#
#         'security_log': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'formatter': 'general_form',
#             'filename': os.path.join(BASE_DIR, 'security.log'),
#         },
#
#         'mail': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'warning_form',
#         },
#     },
#
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'console_warning', 'console_error', 'general_log'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#
#         'django.request': {
#             'handlers': ['mail', 'errors_log'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#
#         'django.server': {
#             'handlers': ['mail', 'errors_log'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#
#         'django.template': {
#             'handlers': ['errors_log'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#
#         'django.db.backends': {
#             'handlers': ['errors_log'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#
#         'django.security': {
#             'handlers': ['security_log'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     },
# }