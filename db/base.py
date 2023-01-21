import sqlite3
from pathlib import Path

DB_NAME = 'db.sqlite3'
MAIN_PATH = Path(__file__).parent.parent
connection = sqlite3.connect(MAIN_PATH/DB_NAME)
cur = connection.cursor()

def create_tables(cur):
    """
    Для создания таблиц 'Товары'
    и 'Заказы' в БД.
    """
    cur.execute(
        """CREAT TABLE product (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    descr TEXT,
    price INTEGER,
    photo TEXT
)

CREAT TABLE orders (
    order_id INTEGER PRIMARY KEY,
    name TEXT,
    userid INTEGER,
    addres INTEGER,
    day TEXT
    product_id INTEGER
    FOREIGN KEY (product_id)
        REFERENSE products(product_id)
)"""
    )
def create_orders(cur):

create_tables(cur)

connection.