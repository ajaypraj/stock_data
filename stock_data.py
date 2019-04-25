# ************************************************************************************************

'''
*********************************************************************************************************
@filename   : stock_data.py
@author     : Ajay Prajapati
@teamLead   : Akash Kamble,Rajesh Dommaraju
@details    : Indian stock details of company like SBI,ITC,RELIANCE etc.
@license    : SpanIdea Systems Pvt. Ltd. All rights reserved.
*********************************************************************************************************
'''

from tkinter import *
from nsepy import get_history
from datetime import datetime
import tkinter.messagebox
import dateutil.relativedelta
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import logging
from tkcalendar import Calendar, DateEntry

# =============================================================
# using Tk we are creating main window
root = Tk()
# Assigning title to stock
root.title("Stock Price calculator")
# Declaring window size
root.geometry("450x220+0+0")
# window resizing is false
root.resizable(width=False, height=False)


# =================logging file name genearte==================
def get_filename_datetime():
    ''' for generating file name
        eg:Stock-2019-04-25 10:39:19.cv
    '''
    now = datetime.now()
    return "Stock-" + now.strftime("%Y-%m-%d %H:%M:%S") + ".csv"


# calling function get_filename_datetime and assigning the file name to name variable
name = get_filename_datetime()

# creating file and configuring logging
'''logging.basicConfig(filename=name, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', filemode="w+")'''

# ===========================================================
# Declaring empty list for storing date
l1 = list()
# Assigning today_date to variable  and x variable is used for setting caldender dates to current
x = datetime.now()


# function to get startdate
def get_startdate():
    def print_sel():
        from_date = cal.selection_get()
        from_date = datetime.strftime(from_date, '%Y,%m,%d')
        from_date = datetime.strptime(from_date, '%Y,%m,%d')
        l1.append(from_date)
        print(l1[0])
        top.destroy()

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=int(x.strftime("%Y")), month=int(x.strftime("%m")), day=int(x.strftime("%d")))
    cal.pack(fill="both", expand=True)

    ttk.Button(top, text="ok", command=print_sel).pack()


l2 = list()


# function to get enddate
def get_enddate():
    def print_sel():
        to_date = cal.selection_get()
        to_date = datetime.strftime(to_date, '%Y,%m,%d')
        to_date = datetime.strptime(to_date, '%Y,%m,%d')
        l2.append(to_date)
        print(l2[0])
        top.destroy()

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=int(x.strftime("%Y")), month=int(x.strftime("%m")), day=int(x.strftime("%d")))
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


# function to get STOCK SYMBOL from menu
def change(*args):
    change.variable = tkvar.get()
    print(change.variable)


# function to get selected date
def change1(*args):
    change1.variable1 = tkvar1.get()
    print(change1.variable1)
    if change1.variable1 == '3 day':
        change1.variable1 = 3
    elif change1.variable1 == '2 day':
        change1.variable1 = 2
    elif change1.variable1 == '7 day':
        change1.variable1 = 7
    elif change1.variable1 == '1 month':
        change1.variable1 = 30
    elif change1.variable1 == '2 month':
        change1.variable1 = 60


# function to get stock symbol details
def getdata():
    print(f1.a)

    if f1.a == 0:
        to_date = datetime.now()

        print(type(to_date))
        to_date = datetime.strftime(to_date, '%Y,%m,%d')
        print(to_date)
        to_date = datetime.strptime(to_date, '%Y,%m,%d')
        print(to_date)
        print(type(to_date))
        print(change1.variable1)
        from_date = to_date - dateutil.relativedelta.relativedelta(days=change1.variable1)
        print(from_date)
        print(from_date, to_date)
    else:
        from_date = l1[0]
        to_date = l2[0]

    print(from_date, to_date)
    try:
        data = get_history(symbol=change.variable, start=from_date, end=to_date)
        print(data[['Close']])
        data[['Close']].plot(grid=True)
        plt.show()
        logging.basicConfig(filename=change.variable+name, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p', filemode="w+")
        logging.info(data.to_csv(name))
    except:
        print("Enter date properly OR Internet connection")


stock = Frame(root, width=400, height=200)
stock.grid()
Label(stock, text="Welcome to Stock Price Viewer", bg="powder blue", font=('arial', 15, 'bold')).grid(row=0, column=0)
Label(stock, text="Select a company Stock Symbol", padx=0, pady=4).grid(row=1, column=0)
Label(stock, text="Select Period of desired stock", padx=0, pady=10).grid(row=2, column=0)
# ===============================stock Symbol pop======================================
tkvar = StringVar(root)
CHOICES = ['SBIN', 'TCS', 'RELIANCE', 'ITC', 'INFY']
tkvar.set('SBIN')  # set the default option

popupMenu = OptionMenu(stock, tkvar, *CHOICES)
tkvar.trace("w", change)
popupMenu.grid(row=1, column=1)


# ==============================================================================================
# function corresponding to first radio button  selection event

def f1(event):
    f1.a = 0
    x1.configure(state=DISABLED)
    x2.configure(state=DISABLED)
    popupMenu2.configure(state=NORMAL)


# function corresponding to first radio button  selection event
def f2(event):
    f1.a = 1
    x1.configure(state=NORMAL)
    x2.configure(state=NORMAL)
    popupMenu2.configure(state=DISABLED)


def message_about():
    return tkinter.messagebox.showinfo("About",
                                       "This is application for viewing past details of stock.It stores stocks and related information file and display graph of stocks as well")


# Assigning new frame
frame2 = Frame(root)
v = IntVar(frame2)
frame2.grid(row=1, column=0)
# defining frame 2 below the frame 1
radio_button = Radiobutton(frame2, text="For Past", padx=20, pady=10, variable=v, value=1)
# binding of radio button click and calling function f1
radio_button.bind('<Button-1>', f1)
# defining Radiobutton for selection of time
radio_button.grid(row=0, column=1)
# defining radiobutton for selection of time span
radio_button1 = Radiobutton(frame2, text="Select a time period", padx=20, pady=10, variable=v, value=2)
radio_button1.grid(row=0, column=2)
# binding of radio button click and calling function f2
radio_button1.bind('<Button-1>', f2)

# ===========Menu for selecting time span===========================================
tkvar1 = StringVar(root)
CHOICES1 = ['3 day', '2 day', '7 day', '1 month', '2 month', '3 month']
tkvar1.set('2 day')
popupMenu2 = OptionMenu(frame2, tkvar1, *CHOICES1)
tkvar1.trace("w", change1)
popupMenu2.grid(row=1, column=1)
# ===================================================================================================
# creating start date button
x1 = Button(frame2, text='Startdate', command=get_startdate)
x1.grid(row=1, column=2)
# creating end date button
x2 = Button(frame2, text='Enddate', command=get_enddate)
x2.grid(row=1, column=3)
# creating get date button
x3 = Button(frame2, text='Get Data', command=getdata)
x3.grid(row=2, column=2)
# =============About menu=================
menubar = Menu(stock)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=message_about)

root.configure(menu=menubar)

# End of main loop
root.mainloop()

