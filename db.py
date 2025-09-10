import os
import mysql.connector

mysql_host     = os.getenv("185.232.14.52")
mysql_user     = os.getenv("u760464709_23005116_usr")
mysql_password = os.getenv("z8[T&05u")
mysql_database = os.getenv("u760464709_23005116_bd")

def get_db():
    return mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
