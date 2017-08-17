import psycopg2

HOST = '172.17.0.3'

connection = psycopg2.connect(host=HOST, user='bar', password='bar', dbname='bar')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS some_table (
        id SERIAL PRIMARY KEY,
        lorem VARCHAR
    );
''')
cursor.execute("INSERT INTO some_table (lorem) VALUES ('ipsum');")
connection.commit()

cursor.execute('SELECT * FROM some_table;')
print(cursor.fetchall())

cursor.close()
connection.close()
