#Pull data
import sqlite3
from sqlite3 import Error
import os.path

#Perform manipulations
import pandas as pd
import numpy as np
import statistics
import datetime

#Visualize data
import seaborn as sns
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters(explicit=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "S&P-500-Stock-Data-(2013-2018).db")
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
except Error as e:
    print(e)


def get_tickets():
    """
    Loop through all the unique tickets and gather them in a name.
    """

    c.execute('SELECT DISTINCT Name FROM "S&P-500"')
    names = c.fetchall()

    tickets = []
    for name in names:
        if name not in tickets:
            tickets.append(name[0])

    return tickets


def calculate_RSI(ticket):
    """
    Pull date, closing prices, and volume values from S&P-500 database to return a dataframe containing the
    items, as well as the calculated 14-day RSI.
    """

    #Data pull
    query = (('SELECT Date, Close, Volume FROM "S&P-500" WHERE Name = "{}"').format(ticket))
    c.execute(query)

    items = c.fetchall()

    ticket_dates = [date[0] for date in items] #ticket datetime
    ticket_prices = [price[1] for price in items] #ticket closing price
    ticket_volumes = [volume[2] for volume in items] #volume of trades for a given ticket

    df = pd.DataFrame(np.column_stack([ticket_dates, ticket_prices, ticket_volumes]), columns=['Dates', 'Prices', 'Volumes'])
    df["Dates"] = pd.to_datetime(df["Dates"])
    df["Prices"] = pd.to_numeric(df["Prices"])
    df["Volumes"] = pd.to_numeric(df["Volumes"])

    #Price change
    price_change = [round(next - current, 4) for current,next in zip(ticket_prices,ticket_prices[1:])] #For each iteration, subtract the current price from the next in the list.  For each difference calculated, round the value to the 4th decimal place

    #Up & Down movement
    UpChange = []
    DownChange = []
    for movement in price_change:
        if movement > 0:
            UpChange.append(movement)
            DownChange.append(0)
        elif movement < 0:
            UpChange.append(0)
            DownChange.append(abs(movement)) #Makes sure that price drops are still represented with positive numbers
        elif movement == 0:
            UpChange.append(0)
            DownChange.append(0)

    #Average Up & Down movement 14-day
    RSI_period = 14

    AvgUpChange = []
    AvgDownChange = []

    initial_avg_up = statistics.mean(UpChange[0:(RSI_period -1)])
    initial_avg_down = statistics.mean(DownChange[0:(RSI_period -1)])

    AvgUpChange.append(initial_avg_up)
    AvgDownChange.append(initial_avg_down)

    for up_value, down_value in zip(UpChange[RSI_period:], DownChange[RSI_period:]):

        avg_up_value = ((AvgUpChange[-1] * 13) + up_value) / 14
        AvgUpChange.append(avg_up_value)

        avg_down_value = ((AvgDownChange[-1] * 13) + down_value) / 14
        AvgDownChange.append(avg_down_value)

        RSI_period += 1

    #Relative Strength Index calculation
    RSI = []
    for u,d in zip(AvgUpChange, AvgDownChange):
        RS = u / d
        final_value = 100 - (100/(RS + 1))
        RSI.append(round(final_value,4))

    df['RSI'] = pd.Series(RSI)

    oversold = []
    overbought = []

    for score in df.RSI:
        if score > 70:
            oversold.append(0)
            overbought.append(score - 70)
        elif score < 30:
            oversold.append(30 - score)
            overbought.append(0)
        elif pd.isnull(score) == True:
            oversold.append(None)
            overbought.append(None)
        else:
            oversold.append(0)
            overbought.append(0)

    df['Oversold'] = pd.Series(oversold)
    df['Overbought'] = pd.Series(overbought)

    return df
