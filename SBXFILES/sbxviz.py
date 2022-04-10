import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql:///?User=postgres&;Password=bkc12278895&Database=sbx_test&Server=localhost&Port=5432")
df = pandas.read_sql("SELECT year, total_waste FROM waste_table", engine)
df.plot(kind="line", x="total_waste",y="year")
plt.show()
