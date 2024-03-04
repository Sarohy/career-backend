"""
Django settings for My_Career_Guidance project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from os import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-07a@z)c3%aqa_-flquq%ni40=)2_m^)$8s&zb9fsl@^p!v%j$7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL='users.User'

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djoser',
    'users',
    'timetable',
    'calculator',
    'cv',
    'psychometric',
    'nested_admin',
    'goals',
    'education',
    'choices',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'My_Career_Guidance.urls'
CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['general/templates'],
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
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '/username/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'ACTIVATION_URL': '/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    "LOGIN_FIELD": "email",
    'SERIALIZERS': {        
        'token_create':'users.serializers.CustomTokenCreateSerializer',
        "user_create": "users.serializers.UserCreateSerializer",
        },
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer'),
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=100),
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'EXCEPTION_HANDLER': 'common.exception_handler.c_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
   
}

# uncomment this code if you want to test in chrome
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'EXCEPTION_HANDLER': 'common.exception_handler.c_exception_handler',
# }

# uncomment this code if you want to test in chrome
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'EXCEPTION_HANDLER': 'common.exception_handler.c_exception_handler',
# }




WSGI_APPLICATION = 'My_Career_Guidance.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':    os.environ['CAREER_DATABASE_NAME'],
        'USER':    os.environ['CAREER_DATABASE_USER'],
        'PASSWORD': os.environ['CAREER_DATABASE_PASS'],
        'HOST': os.environ['CAREER_DATABASE_HOST'],
        'PORT': os.environ['CAREER_DB_PORT'],
    }
}


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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "media/"
MEDIA_ROOT = "media"
AWS_ACCESS_KEY_ID = os.environ['CAREER_GUIDANCE_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['CAREER_GUIDANCE_AWS_SECRET_KEY_ID']
# AWS_STORAGE_BUCKET_NAME = 'CGB-Staging-Bucket'
DOMAIN = 'https://us-east-1.console.aws.amazon.com/amplify/home?region=us-east-1#/d2eqtmfyvf15r'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
DATA_UPLOAD_MAX_MEMORY_SIZE = 100000000
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000  # Or any desired higher value


AWS_STORAGE_BUCKET_NAME = 'cgb-staging-bucket'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# SMTP email service
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ['EMAIL_HOST_USER']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']