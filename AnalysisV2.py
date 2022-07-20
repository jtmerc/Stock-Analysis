# [1] Import modules - run jupyter lab
import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY

# [2] Date
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2022, 7, 1)

# [3] Multiple Stocks
gme = web.DataReader("GME", "yahoo", start, end)
tesla = web.DataReader("TSLA", "yahoo", start, end)
bmw = web.DataReader("BMW.DE", "yahoo", start, end)
mercedes = web.DataReader("DDAIF", "yahoo", start, end)

# [4] save to csv
gme.to_csv('Gamestop Stock from 2018 to 2022')
tesla.to_csv('Tesla Stock from 2018 to 2022')
bmw.to_csv('BMW Stock from 2018 to 2022')
mercedes.to_csv('Mercedes Stock from 2018 to 2022')

# [5] head
gme.head()
tesla.head()
bmw.head()
mercedes.head()

# [6] tail
gme.tail()
tesla.tail()
bmw.tail()
mercedes.tail()

# [7] close
gme['Close'].plot(label='GME at Closing', figsize=(16, 5))
tesla['Close'].plot(label='Tesla at Closing')
bmw['Close'].plot(label='BMW at Closing')
mercedes['Close'].plot(label='Mercedes at Closing')
plt.legend()
plt.title('Interested Stocks')
plt.ylabel('Stock Prices')
plt.show()

# [8] open
gme['Open'].plot(label='GME at Opening', figsize=(16, 5))
tesla['Open'].plot(label='Tesla at Opening')
bmw['Open'].plot(label='BMW at Opening')
mercedes['Open'].plot(label='Mercedes at Opening')
plt.legend()
plt.title('Interested Stocks')
plt.ylabel('Stock Prices')
plt.show()

# [9] volume
gme['Volume'].plot(label='GME Volume', figsize=(16, 5))
tesla['Volume'].plot(label='Tesla Volume')
bmw['Volume'].plot(label='BMW Volume')
mercedes['Volume'].plot(label='Mercedes Volume')
plt.legend()
plt.title('Interested Stocks')
plt.ylabel('Stock Prices')
plt.show()

# [10] Individual open mid-2020
gme.iloc[1300:2000]['Open'].plot(figsize=(16, 5))

# [11] Individual open 2020
gme.iloc[1300:1400]['Open'].plot(figsize=(16, 5))

# [12] Market cap
gme['Total Traded'] = gme['Open'] * gme['Volume']
tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
bmw['Total Traded'] = bmw['Open'] * bmw['Volume']
mercedes['Total Traded'] = mercedes['Open'] * mercedes['Volume']
# [13]
gme

# [14] Market cap chart
gme['Total Traded'].plot(label='GME Total Traded', figsize=(16, 5))
tesla['Total Traded'].plot(label='Tesla Total Traded')
bmw['Total Traded'].plot(label='BMW Total Traded')
mercedes['Total Traded'].plot(label='Mercedes Total Traded')
plt.legend()
plt.title('Interested Stocks')
plt.ylabel('Total Traded')
plt.show()

# [15]
gme['Total Traded'].argmax()
# [16]
gme.iloc[[gme['Total Traded'].argmax()]]

# [17] Moving average
gme['Close'].plot(label='Gamestop Stock at Close', figsize=(16, 5))
tesla['Close'].plot(label='Tesla Stock at Close', figsize=(16, 5))
bmw['Close'].plot(label='BMW Stock at Close', figsize=(16, 5))
mercedes['Close'].plot(label='Mercedes Stock at Close', figsize=(16, 5))

# [18]
gme['Close'].plot(figsize=(16, 5))
gme['MA60'] = gme['Close'].rolling(60).mean()
gme['MA60'].plot(label='MA60')
gme['Close'].plot(label='No moving average', figsize=(16, 5))
gme['MA300'] = gme['Close'].rolling(300).mean()
gme['MA300'].plot(label='MA300')
plt.legend()

# [19]
# from pandas.plotting import scatter_matrix
# import pandas as pd

# [20]
in_stock = pd.concat([gme['Close'], tesla['Close'], bmw['Close'], mercedes['Close']], axis=1)
in_stock.columns = ['Gamestop Open', 'Tesla Open', 'BMW Open', 'Mercedes Open']

# [21]
scatter_matrix(in_stock, figsize=(16, 5))

# [22] Candle stick charts
# from mpl_finance import candlestick_ohlc
# from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY

# [23]
gme_reset = gme.loc['2021-12-01': '2021-12-16'].reset_index()

# [24]
gme_reset['data_acc'] = gme_reset['Date'].apply(lambda date: date2num(date))
gme_values = [tuple(vals) for vals in
              gme_reset[['date_acc', 'Open', 'High', 'Low', 'Close']].values]
mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')
fig, acc = plt.subplots()
candlestick_ohlc(gme, gme_values, width=0.6, colorup='g', colordown='b')

# [25]
gme['returns'].hist(bins=50)

# [26]
gme['returns'].hist(bins=100, label='GME')
tesla['returns'].hist(bins=50, label='Tesla')
bmw['returns'].hist(bins=50, label='BMW')
mercedes['returns'].hist(bins=50, label='Mercedes')
plt.legend()

# [27]
gme['returns'].plot(kind='kde', label='GME')
tesla['returns'].plot(kind='kde', label='Tesla')
bmw['returns'].plot(kind='kde', label='BMW')
mercedes['returns'].plot(kind='kde', label='Mercedes')
plt.legend()

# [28] Box Plots
box_df = pd.concat([gme['returns'], tesla['returns'], bmw['returns'], mercedes['returns']], axis=1)
box_df.columns = ['GME', 'Tesla', 'BMW', 'Mercedes']
box_df.plot(kind='box', figsize=(16, 5))

# [29] Cumulative return
gme['Cumulative Return'].plot(label='GME', figsize=(16, 5))
tesla['Cumulative Return'].plot(label='Tesla')
bmw['Cumulative Return'].plot(label='BMW')
mercedes['Cumulative Return'].plot(label='Mercedes')
plt.title('Cumulative Return vs Time')
plt.legend()
