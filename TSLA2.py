import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020, 1, 3)
end = dt.datetime.now()
df = web.DataReader("TSLA", 'yahoo', start, end)
print(df.head())


df.to_csv('TSLA.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
df['Open'].plot()
plt.show()