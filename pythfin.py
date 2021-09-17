import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2000,1,1)
#end = dt.datetime(2016,12,31)

#df = web.DataReader('TSLA', 'yahoo', start, end)

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col = 0)
#print (df.head())
mpf.plot(df,type='candle',mav=10,volume=True,figratio=(11,8),figscale=.85,style='yahoo')
#df['Adj Close'].plot()
#plt.show()

#df['100ma'] = df['Adj Close'].rolling(window=100).mean()
#df.dropna(inplace=True)

#df_ohlc = df['Adj Close'].resample('10D').ohlc()
#df_volume = df['Volume'].resample('10D').sum()

#df_ohlc.reset_index(inplace=True)

#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#print (df_ohlc.head())


#ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)
#ax1.xaxis_date()

#candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
#ax1.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

#plt.show()