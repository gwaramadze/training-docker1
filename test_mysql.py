import pymysql

HOST = '172.17.0.4'

connection = pymysql.connect(host=HOST, user='bar', password='bar', db='bar')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS some_table (
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        lorem VARCHAR(5)
    );
''')
cursor.execute("INSERT INTO some_table (lorem) VALUES ('ipsum');")
connection.commit()

cursor.execute('SELECT * FROM some_table;')
print(cursor.fetchall())

cursor.close()
connection.close()
