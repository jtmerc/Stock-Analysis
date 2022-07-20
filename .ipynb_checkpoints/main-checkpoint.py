# Import modules
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

start = "2020-01-01"
end = '2022-7-01'
gme = yf.download('GME', start, end)
infy = yf.download('INFY', start, end)
wipro = yf.download('WIPRO.NS', start, end)

# Open
gme['Open'].plot(label='GME', figsize=(15, 7))
infy['Open'].plot(label="Infosys")
wipro['Open'].plot(label='Wipro')
plt.title('Stock Prices of GME, Infosys and Wipro')


# Volume
gme['Volume'].plot(label='GME', figsize=(15, 7))
infy['Volume'].plot(label="Infosys")
wipro['Volume'].plot(label='Wipro')
plt.title('Volume of Stock traded')
plt.legend()

# Market Capitalisation
gme['MarktCap'] = gme['Open'] * gme['Volume']
infy['MarktCap'] = infy['Open'] * infy['Volume']
wipro['MarktCap'] = wipro['Open'] * wipro['Volume']
gme['MarktCap'].plot(label='GME', figsize=(15, 7))
infy['MarktCap'].plot(label='Infosys')
wipro['MarktCap'].plot(label='Wipro')
plt.title('Market Cap')
plt.legend()

gme['MA50'] = gme['Open'].rolling(50).mean()
gme['MA200'] = gme['Open'].rolling(200).mean()
gme['Open'].plot(figsize=(15, 7))
gme['MA50'].plot()
gme['MA200'].plot()

# Volatility
gme['returns'] = (gme['Close']/gme['Close'].shift(1)) - 1
infy['returns'] = (infy['Close']/infy['Close'].shift(1))-1
wipro['returns'] = (wipro['Close']/wipro['Close'].shift(1)) - 1
gme['returns'].hist(bins=100, label='TCS', alpha=0.5, figsize=(15, 7))
infy['returns'].hist(bins=100, label='Infosysy', alpha=0.5)
wipro['returns'].hist(bins=100, label='Wipro', alpha=0.5)
plt.legend()
