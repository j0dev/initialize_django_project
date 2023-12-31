# system
import os
import ast


class SERVICE:
    # Service CONFIG
    DEBUG = int(os.environ.get("DEBUG", False))  # DEBUG MODE
    SERVICE_NAME = os.environ.get("DJANGO_SVC_NAME")  # SERVICE NAME
    HOST = "dev" if DEBUG else "prod"  # SERVICE HOST (DOMAIN)
    SECRET_KEY = os.environ.get("SECRET_KEY")  # SERVICE SECRET KEY
    CORS_ORIGIN_WHITELIST = ast.literal_eval(os.environ.get("CORS_ORIGIN_WHITELIST"))  # CORS WHITE LIST
    ACCESS_TOKEN_EXP_MIN = int(os.environ.get("ACCESS_TOKEN_EXP_MIN"))  # ACCESS TOKEN EXPIRE MININUTE
    REFRESH_TOKEN_EXP_DAY = int(os.environ.get("REFRESH_TOKEN_EXP_DAY"))  # REFRESH TOKEN EXPIRE DAYS


class DATABASE:
    # DATABASE CONFIG
    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_TEST_NAME = os.environ.get("DB_TEST_NAME")


class SYSTEM_CODE:
    # 0 ~ 999 : DEFAUT SYSTEM CODE
    SUCCESS = (0, "SUCCESS")
    CLIENT_ERROR = (1, "CLIENT_ERROR")
    UNKNOWN_SERVER_ERROR = (2, "UNKNOWN_SERVER_ERROR")
    INVALID_FORMAT = (3, "INVALID_FORMAT")
    OBJECT_DOES_NOT_EXIST = (4, "OBJECT_DOES_NOT_EXIST")

    # 1000 ~ 1999 : AUTH
    AUTH_REQUIRED = (1000, "AUTH_REQUIRED")
    TOKEN_INVALID = (1001, "TOKEN_INVALID")
    TOKEN_EXPIRED = (1002, "TOKEN_EXPIRED")
    EMAIL_PASSWORD_MISMATCH = (1003, "EMAIL_PASSWORD_MISMATCH")
    EMAIL_ALREADY_USE = (1004, "EMAIL_ALREADY_USE")
    EMAIL_NOT_FOUND = (1005, "EMAIL_NOT_FOUND")

    # 2000 ~ 2999 : USER
    USER_NOT_FOUND = (2000, "USER_NOT_FOUND")

    # 3000 ~3999 : ARTICLE
    ARTICLE_NOT_FOUND = (3000, "ARTICLE_NOT_FOUND")
