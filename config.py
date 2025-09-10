import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secreto")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "185.232.14.52")
    MYSQL_USER = os.getenv("MYSQL_USER", "u760464709_23005116_usr")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "z8[T&05u")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "u760464709_23005116_bd")
    DEBUG = os.getenv("FLASK_DEBUG", True)
