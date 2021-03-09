import psycopg2, psycopg2.extras

DB_HOST = '127.0.0.1'
DB_USER = 'postgres'
DB_NAME = 'fin_db'
DB_PASS = 'password'

connection = psycopg2.connect(
    host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
)

cursor = connection.cursor(cursor_factory=psycopg2.cursor.extras.DictCursor)