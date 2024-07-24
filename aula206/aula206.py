import os
import pymysql
import dotenv

dotenv.load_dotenv()

connection = pymysql.connect(
    host = 'localhost',
    user = 'usuario',
    password = 'senha', 
    database = 'base_de_dados',
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSQORD'],
    database=os.environ['MYSQL_DATABASE']
)

with connection:
    with connection.cursor() as cursor:
        print(cursor)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
        'CREATE TABLE IF NOT EXISTIS customers, '
        'id INT NOT NULL AUTO_INCREMET, '
        'nome VARCHAR(50) NOT NULL, '
        'idade INT NOT NULL, '
        'PRIMARY KEY (id)'
        ') '
    )
    print(cursor)

