# coding=UTF-8
"""

Django settings for wasu project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'debsv6v89f^!c!-bcwpnh-)gp8183519*$y8+71l1!k17-#wtg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'boss',
    'rmss',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wasu.urls'

WSGI_APPLICATION = 'wasu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'boss':{
        'ENGINE':'django.db.backends.oracle',
        'NAME':'boss',
        'USER':'sm',
        'PASSWORD':'sm',
        'HOST':'125.210.208.69',
        'PORT':'1521',
        },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR,'rmss/templates'),
        )

ENABLE  = u'启用'
DISABLE = u'未启用'
UNDO    = u'撤销'
MACHINE_ROOM_CHOICES = ((ENABLE,u'启用'),(DISABLE,'未启用'),(UNDO,'撤销'),)

YES = u'是'
NO  = u'否'
MONIROTING_CHOICES = ((YES,u'是'),(NO,u'否'),)

AC = u'交流'
DC = u'直流'
BATTERY_TYPE_CHOICES = ((AC,u'交流'),(DC,u'直流'),)

SINGLE = u'单路供电'
DUAL   = u'双路供电'
POWER_SUPPLY_CHOICES = ((SINGLE,u'单路供电'),(DUAL,u'双路供电'),)

HAVE = u'有'
NOT_HAVE = u'无'
INTERFACE_CHOICES = ((HAVE,u'有'),(NOT_HAVE,u'无'),)

A10 = '10A'
A16 = '16A'
A32 = '32A'
A64 = '64A'
AIR_SWITCH_CONFIGURATION_CHOICES = ((A10,'10A'),(A16,'16A'),(A32,'32A'),(A64,'64A'),)
