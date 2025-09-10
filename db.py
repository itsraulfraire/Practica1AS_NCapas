import psycopg2

def get_db():
    return psycopg2.connect(
        host="185.232.14.52",
        user="u760464709_23005116_usr",
        password="z8[T&05u",
        dbname="u760464709_23005116_bd"
    )
