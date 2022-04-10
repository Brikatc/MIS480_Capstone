import psycopg2
conn = psycopg2.connect(database="sbx_test", user='postgres',
                        password='bkc!12278895', host='localhost', port='5432')

cursor = conn.cursor()
cursor.execute("select version()")
cursor.execute("SELECT * FROM waste_table")
print(cursor.fetchall())

cursor.close()
conn.close()
