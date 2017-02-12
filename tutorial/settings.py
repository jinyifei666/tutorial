"""
Django settings for tutorial project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import logging
from registration_defaults.settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '79d@j^tujmpuq9wn@3lk*4ftn1gu1!3%kd2v1d2zqedsxxl1og'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["202.114.106.24","127.0.0.1","192.168.1.106","202.114.107.185","jinyifei.imwork.net"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quickstart',
    'rest_framework',

    'registration',
    'registration_defaults',

     'tagging',
     'social.apps.django_app.default',
     'django.contrib.sites',
    #
    # 'rest_framework.authtoken',
    # 'rest_auth',
    # 'rest_auth.registration',
    #
    # 'allauth',
     'allauth.account',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.weixin',
    # 'rest_framework_swagger',
    'captcha',


]


SITE_ID = 1
LOGIN_REDIRECT_URL = '/api'

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'




REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),    #管理员可登陆
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    #'DEFAULT_PERMISSION_CLASSES': [ 'rest_framework.permissions.IsAuthenticatedOrReadOnly'],  # 所有人可查看，但是只有登陆用户才可以修改
#    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],     #查看官方文档，需要在model中定义
    'PAGE_SIZE': 10
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


#调试设置
logging.basicConfig(
    level = logging.DEBUG,
    format ='%(asctime)s %(levelname)s %(message)s',
)



SOCIALACCOUNT_PROVIDERS = {
    'weixin': {
        'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/oauth2/authorize', # for media platform
    }
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'login',
    'LOGOUT_URL': 'logout',
}

ROOT_URLCONF = 'tutorial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.request',

            ],

        },
    },
]

OLD_PASSWORD_FIELD_ENABLED = True

WSGI_APPLICATION = 'tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'#'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'Media')
MEDIA_URL  = '/Media/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  'static'),
)


#电子邮件
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.sina.com'                   #SMTP地址
EMAIL_PORT='587'
EMAIL_HOST_USER='jinyifei1020@sina.com'
EMAIL_HOST_PASSWORD='******'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='jinyifei1020@sina.com'
#管理员站点
SERVER_EMAIL = 'jinyifei1020@sina.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

app_key = u'a66fed1923c9c82b2db79db7'
master_secret = u'6ca581e3da795f787a872051'
