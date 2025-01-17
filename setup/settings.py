"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
from enum import Enum

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1", "34.95.227.96"]

CSRF_TRUSTED_ORIGINS = ["http://34.95.227.96"]


# Application definition

MY_APPS = [
    "challenges",
    "users",
    "theme",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "tailwind",
    "django_browser_reload",
    "django_components",
    "crispy_forms",
    "crispy_tailwind",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # necessary for allauth
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

THIRD_PARTY_MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DJANGO_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                        "django_components.template_loader.Loader",
                    ],
                )
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Database(Enum):
    PROD = "prod"
    DEV = "dev"


database_choice = config("DJANGO_DB", default=Database.DEV.value)

db = {
    Database.PROD.value: {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    },
    Database.DEV.value: {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}

DATABASES = {}
if database_choice in db:
    DATABASES["default"] = db[database_choice]
else:
    raise KeyError(f"Invalid DJANGO_DB value: {database_choice}")


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, "static/")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

# Additional locations of static files to django_components
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "components"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Allauth settings

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Tailwind settings

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]


# Crispy forms settings

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Image settings

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
