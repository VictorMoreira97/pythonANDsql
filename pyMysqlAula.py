import os
import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host='localhost',
    user='usurio',
    password='senha',
    database='base_de_dados',
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with connection.cursor() as cursor:
    # SQL
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE customers('
            f'CREATE TABLE IF NOT EXISTIS {TABLE_NAME}'
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
        )
    print(cursor)
    connection.commit()

with connection.cursor() as cursor:
    result = cursor.execute(
        f'INSERT INTO {TABLE_NAME}'
        '(nome, idade) VALUES ("Luiz", 25)'
    )
    print(result)
connection.commit()