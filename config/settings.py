import os
from datetime import timedelta
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="").split(" ")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # packages
    "rest_framework",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
    "djoser",
    # My apps
    "api",
    "common",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
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


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("PG_DATABASE", "postgres"),
        "USER": config("PG_USER", "postgres"),
        "PASSWORD": config("PG_PASSWORD", "postgres"),
        "HOST": config("DB_HOST", "localhost"),
        "PORT": config("DB_PORT", 5432),
    },
    "extra": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}


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


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# RESTFRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# DJOSER
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "SERIALIZERS": {},
}


# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),
}


# DRF_SPECTACULAR
SPECTACULAR_SETTINGS = {
    "TITLE": "Call Helper",
    "DESCRIPTION": "Call Helper",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "SERVE_AUTHENTICATION": [
        "rest_framework.authentication.BasicAuthentication",
    ],
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayOperationId": True,
        "syntaxHighlight.active": True,
        "syntaxHighlight.theme": "arta",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "filter": True,
        "requestSnippetsEnabled": True,
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "SORT_OPERATIONS": False,
    "ENABLE_DJANGO_DEPLOY_CHECK": False,
    "DISABLE_ERRORS_AND_WARNINGS": True,
}


# LOCALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# STATIC MEDIA
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "/media/"
MEDIA_TEST_ROOT = os.path.join(BASE_DIR, "media/test/")


# CORS HEADERS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS__ALLOW_HEADERS = ["*"]
CSRF_COOKIE_SECURE = False
