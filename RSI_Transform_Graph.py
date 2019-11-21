from datetime import datetime

#Visualisation imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
pd.plotting.register_matplotlib_converters(explicit=True)
plt.style.use('seaborn')
sns.set_style('darkgrid')

#Data imports
from DB_Query import calculate_RSI
from stock_ticker import chosen_ticker

stock = chosen_ticker()
df = calculate_RSI(stock)

#print_headmap = input('Graph heatmap? (y/n): ')
print (df)


def RSI_linegraph(df):
    linegraph = sns.lineplot(x = df.index, y = df.RSI)
    linegraph.axhline(70, ls='-', c = 'grey')
    linegraph.axhline(30, ls='-', c = 'grey')
    plt.show()

def RSI_heatmap(df):
    data = [df["Price"]]
    ax = sns.heatmap(data)
    plt.show()


RSI_linegraph(df)
RSI_heatmap(df)
