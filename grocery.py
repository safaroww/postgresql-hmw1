from django.db import connection
import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='asif2017',
    host='localhost',
    port='5432',
    database='grocery_db'
)


cursor = connection.cursor()


query = """
CREATE TABLE employee(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    stock INT DEFAULT 0,
    is_new BOOLEAN NOT NULL,
    worker_id SERIAL UNIQUE NOT NULL,
    release DATE,
    release_time DATE,
    exp_date DATE,
    price INT NOT NULL,
    sales_num INT DEFAULT 0 NOT NULL,
    bar_code INT UNIQUE NOT NULL
)
"""

cursor.execute()

connection.commit()