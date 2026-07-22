import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
TSM = yf.Ticker("TSM")
data = TSM.history(period="1y")
print(data[["Open", "Close", "High", "Low", "Volume"]])

data["ShortMovAvg"] = data["Close"].rolling(7).mean()
data["LongMovAvg"] = data["Close"].rolling(28).mean()

data["Signal"] = 0
data.loc[data["ShortMovAvg"] > data["LongMovAvg"], "Signal"] = 1

print(data)

compare = data["Signal"].diff()
data["Action"] = "Утримання"
data.loc[compare < 0, "Action"] = "Продаж"
data.loc[compare > 0, "Action"] = "Купівля"