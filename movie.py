import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='asif2017',
    host='localhost',
    port='5432',
    database='movie'
)


cursor = connection.cursor()

query = """
CREATE TABLE hmw(
    id SERIAL PRIMARY KEY,
    film_name VARCHAR(50) NOT NULL,
    description TEXT,
    views INT NOT NULL DEFAULT 0,
    janr_id SERIAL UNIQUE NOT NULL,
    release_date DATE NOT NULL,
    has_fragman BOOLEAN DEFAULT false
)   
"""


cursor.execute(query)

connection.commit()