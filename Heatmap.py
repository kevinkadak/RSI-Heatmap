#Visualisation imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')

#DB_Query functions
from DB_Query import get_tickets, calculate_RSI

stock = "NVDA"

stock_tickets = get_tickets()
df = calculate_RSI(stock)

#sns.heatmap([df.RSI, df.Volumes], annot=True)
#sns.lmplot(x = df.Volumes, y = df.Prices, data = df)
#plt.show()

print (df)

#Plotting the total volume being traded over time
#dataframe['Volumes'].plot(legend=True,figsize=(12,5))


#print (oversold)

'''
plt.figure(figsize=(9,9))
pivot_table = phase_1_2.pivot('helix1 phase', 'helix 2 phase','Energy')
plt.xlabel('helix 2 phase', size = 15)
plt.ylabel('helix1 phase', size = 15)
plt.title('Energy from Helix Phase Angles', size = 15)
sns.heatmap(pivot_table, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r');

'''
