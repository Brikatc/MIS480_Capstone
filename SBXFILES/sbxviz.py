import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from matplotlib import interactive

conn = psycopg2.connect(database="sbx_test", user='postgres',
                        password='bkc!12278895', host='localhost', port='5432')
sql = "SELECT * FROM waste_table"
dat = pd.read_sql_query(sql, conn)
df = pd.DataFrame(dat, columns=["year","total_waste","total_previous_year","percent_change"])
print(df.head())
p_line1=dat.plot(kind="line", x="year", y="total_waste")
plt.figure(1)
p_bar1=dat.plot(kind="bar", x="year", y="total_waste")
plt.figure(2)
p_line2=dat.plot(kind="line", x="year", y="percent_change")
plt.figure(3)
p_bar2=dat.plot(kind="bar", x="year", y="percent_change")
plt.figure(4)
print(df.describe())
print(df.std())
plt.show()



