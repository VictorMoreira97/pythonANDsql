import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR/DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: DELETE sem WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Criar tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTIS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabelas
# CUIDADO: sql injetion
cursor.execute(
    f'INSERT INTO {TABLE_NAME}'
    '(id, name, wight) '
    'VALUES '
    '(NULL, "Helena", 4), (NULL, "eDUARDO", 10)'
)
connection.commit()

cursor.close()
connection.close()