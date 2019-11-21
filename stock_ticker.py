from DB_Query import get_tickers
from tkinter import *


tickers = get_tickers()
print (tickers)

def chosen_ticker():
    stock = input("Input stock ticker: ")
    return stock


# Tkinter item selection GUI
# master = Tk()
#
# listbox = Listbox(master, selectmode = 'SINGLE')
# listbox.pack()
#
# listbox.insert(END, "a list entry")
#
# for item in tickers:
#     listbox.insert(END, item)
#
# mainloop()
