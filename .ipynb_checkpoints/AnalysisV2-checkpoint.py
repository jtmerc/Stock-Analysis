# Import modules
import pandas_datareader.data as web
import datetime
import pandas as pd

# Date
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2022, 7, 1)

# Ticker
bmw = web.DataReader("BMW.DE", "yahoo", start,end)
bmw
