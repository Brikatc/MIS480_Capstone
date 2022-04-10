import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

conn = psycopg2.connect(database="sbx_test", user='postgres',
                        password='bkc!12278895', host='localhost', port='5432')
sql = "SELECT * FROM waste_table"
dat = pd.read_sql_query(sql, conn)
df = pd.DataFrame(dat, columns=["year","total_waste","total_previous_year","percent_change"])
print(df)
dat.plot(kind="line", x="year", y="total_waste")
plt.show()
dat.plot(kind="line", x="year", y="percent_change")
plt.show()
print(df.describe())
