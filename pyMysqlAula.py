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
    sql = (
        f'INSERT INTO {TABLE_NAME}'
        '(nome, idade)'
        'VALUES '
        '(%s, %s)'
    )
    data2 = (
        {"name": "Siri", "age": 22, },
        {"name": "Helena", "age": 15, },
    )
    result = cursor.execute(sql, data2)
    print(sql)
    print(data2)
    print(result)
connection.commit()

with connection.cursor() as cursor:
        sql = (
             f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql)

data4 = (
     ("Siri", 22, ),
     ("Helena", 15, ),
     ("Luiz", 18, ),
)
result = cursor.executemany(sql, data4)

with connection.cursor() as cursor:
     menor_id = int(input('Digite o menor id: '))
     maior_id = int(input('Digite o maior id: '))

     sql = (
          f'SELECT * FROM {TABLE_NAME}'
          'WHERE id BETWEEN %s AND %s'
     )
     cursor.execute(sql)

     cursor.execute(sql, (menor_id, maior_id))
     print(cursor.mogrify(sql, (menor_id, maior_id)))
     data5 = cursor.fetchall()

connection.commit()

with connection.cursor() as cursor:
     id_recebido = input('Digite um id: ')
     coluna = 'id'
     sql = (
          f'SELECT * FROM {TABLE_NAME}'
          f'WHERE {coluna} = %s '
     )
     cursor.execute(sql, (id_recebido,))
     print(cursor.mogrify(sql, (id_recebido,)))
     data5 = cursor.fetchall()

     for row in data5:
          print(row)
