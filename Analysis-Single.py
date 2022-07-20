# [1] Import modules - run jupyter lab
import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance

# [2] Date
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2022, 7, 1)

# [3] Ticker
gme = web.DataReader("GME", "yahoo", start, end)

# [4]
gme

# [5]
gme.head()

# [6]
gme.tail()

# [7]
gme['Close'].plot()
plt.show()

# [8]
gme['Close'].plot(label='Stocks at Closing', figsize=(16, 5))
gme['Open'].plot(label='Stocks at Opening')
gme['High'].plot(label='Stocks a High')
gme['Low'].plot(label='Stocks a Low')
plt.legend()
plt.title('GME stock prices')
plt.ylabel('Stock Prices')
plt.show()

