import matplotlib.pyplot as plt 
import datetime as dt 
import pandas as pd 

date1 = dt.datetime(2015, 5, 26)
date2 = dt.datetime(2015, 5, 29)

xdates = pd.date_range(date1, date2)
yvals = [10,25,15,20]

plt.title("Time-Series")
plt.xlabel("Dates")
plt.ylabel('values')

plt.plot_date(xdates, yvals)

plt.legend("Time-Series Plot")

plt.show()