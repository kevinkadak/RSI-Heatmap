from datetime import datetime

#Visualisation imports
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
pd.plotting.register_matplotlib_converters(explicit=True)
sns.set_style('darkgrid')

#DB_Query functions
from DB_Query import get_tickers, calculate_RSI

stock = "AAPL"

stock_tickers = get_tickers()
df = calculate_RSI(stock)

print (df)

#sns.heatmap([df.RSI, df.Volumes], annot=True)
#sns.lmplot(x = df.Volumes, y = df.Prices, data = df)
#plt.show()

def RSI_linegraph(df):
    linegraph = sns.lineplot(x = df.Dates, y = df.RSI)
    linegraph.axhline(70, ls='--')
    linegraph.axhline(30, ls='--')
    plt.show()

def RSI_heatmap(df):
    #ax = sns.heatmap([x = df.Prices, y = df.Volumes, df.RSI])
    plt.show()

RSI_heatmap(df)
