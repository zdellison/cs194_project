"""
Django settings for tweetboard project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')_8r2g^k@-9#9=@k!7@ayru5&0m=e#b$c@y=2+4cd75k_6$g)h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # NOTE: Not using social_auth anymore
    #    'social_auth',
    'login',
    'dashboard',
    'api'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tweetboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
		'login/templates',
		'dashboard/templates',
		'tweetboard/templates',
	    ],
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

WSGI_APPLICATION = 'tweetboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# NOTE: Not using the social_auth package anymore...

# Set up Authentication Backends, specifically for Twitter Auth
# Based on dependency for Django Social Auth

#AUTHENTICATION_BACKENDS = (
#   'social_auth.backends.twitter.TwitterBackend',
#   #'social_auth.backends.facebook.FacebookBackend',
#   #'social_auth.backends.google.GoogleOAuthBackend',
#   #'social_auth.backends.google.GoogleOAuth2Backend',
#   #'social_auth.backends.google.GoogleBackend',
#   #'social_auth.backends.yahoo.YahooBackend',
#   #'social_auth.backends.browserid.BrowserIDBackend',
#   #'social_auth.backends.contrib.linkedin.LinkedinBackend',
#   #'social_auth.backends.contrib.disqus.DisqusBackend',
#   #'social_auth.backends.contrib.livejournal.LiveJournalBackend',
#   #'social_auth.backends.contrib.orkut.OrkutBackend',
#   #'social_auth.backends.contrib.foursquare.FoursquareBackend',
#   #'social_auth.backends.contrib.github.GithubBackend',
#   #'social_auth.backends.contrib.vk.VKOAuth2Backend',
#   #'social_auth.backends.contrib.live.LiveBackend',
#   #'social_auth.backends.contrib.skyrock.SkyrockBackend',
#   #'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
#   #'social_auth.backends.contrib.readability.ReadabilityBackend',
#   #'social_auth.backends.contrib.fedora.FedoraBackend',
#   #'social_auth.backends.OpenIDBackend',
#   'django.contrib.auth.backends.ModelBackend',
#)

# Authentication Keys for Twitter App Authentication

TWITTER_CONSUMER_KEY         = 'JxN0e4UadwteFOhoXWdCWgeVu'
TWITTER_CONSUMER_SECRET      = '1juniHyavCPMr8bM9l22uFqrNHXghDSLc8fZWuIlV0qaoniW6n'

# Login settings as described by Twitter App Authentication

LOGIN_URL          = '/login/'

AUTH_PROFILE_MODULE = 'login.Profile'
