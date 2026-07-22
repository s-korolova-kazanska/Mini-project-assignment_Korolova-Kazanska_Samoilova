import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
TSM = yf.Ticker("TSM")
data = TSM.history(period="1y")
print(data[["Open", "Close", "High", "Low", "Volume"]])
