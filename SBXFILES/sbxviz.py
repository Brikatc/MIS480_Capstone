import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

conn = psycopg2.connect(database="sbx_test", user='postgres',
                        password='bkc!12278895', host='localhost', port='5432')
sql = "SELECT * FROM waste_table"
dat = pd.read_sql_query(sql, conn)
dat.plot(kind="bar", x="year", y="total_waste")
plt.show()
