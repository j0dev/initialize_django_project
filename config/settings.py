"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# System
from pathlib import Path
import os

# Project
from config.constants import SERVICE, DATABASE

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SERVICE.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SERVICE.DEBUG

ALLOWED_HOSTS = ["*"]  # ALLOLW HOST (Set when host fixed)


# Application definition

INSTALLED_APPS = [
    # SYSTEM
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "drf_yasg",
    # APPs
    "apps",
    "apps.users",
    "apps.systems",
    "apps.articles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DATABASE.DB_NAME,
        "USER": DATABASE.DB_USER,
        "PASSWORD": DATABASE.DB_PASSWORD,
        "HOST": DATABASE.DB_HOST,
        "PORT": DATABASE.DB_PORT,
        "TEST": {
            "NAME": DATABASE.DB_TEST_NAME,
        },
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'", "charset": "utf8mb4", "use_unicode": True},
    }
}

AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DRF SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "config.rest_framework.CustomJWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "EXCEPTION_HANDLER": "config.rest_framework.cusotm_api_exception_handler",
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
}


# CORS
CORS_ORIGIN_WHITELIST = SERVICE.CORS_ORIGIN_WHITELIST

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]


# SWAGGER
SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "config.swaggers.custom_schema.CustomSwaggerAutoSchema",
    "DEFAULT_MODEL_RENDERING": "scheme",
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        },
    },
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "time-prefixed": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "syslog": {
            "level": "DEBUG",
            "class": "logging.handlers.SysLogHandler",  # TODO: filebeat, logstash 사용하도록 변경
            "formatter": "time-prefixed",
        },
        "sql": {
            "level": "DEBUG",
            "class": "logging.handlers.SysLogHandler",
            "formatter": "time-prefixed",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs"),
            "formatter": "time-prefixed",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["syslog", "file"],
            "level": "INFO",
        },
        "django.db.backends": {
            "handlers": ["sql", "file"],
            "level": "ERROR",
        },
    },
}
