
import pandas_datareader.data as pdr
import yfinance as yf
from datetime import date
import csv


def get_data(symbols, d0, d1, period):
    yf.pdr_override()
    stocks = pdr.get_data_yahoo(symbols, d0, d1, interval=period, as_panel=False)
    return stocks

with open('b3symbols.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

symbols = [''.join(x) for x in data]

d0 = date(2021, 4, 20)
d1 = date.today()

stocks = get_data(symbols,d0, d1, '1d')