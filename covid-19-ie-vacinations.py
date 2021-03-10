from matplotlib import pyplot as plt
import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import jinja2
import matplotlib.dates as mdates

# Get latest data in csv format
filename = 'covid-19-ie-vacinations-raw.csv'

df = pd.read_csv(filename)

# Calculations
df["DosesToday"] = df["TotalDoses"].diff()
df["FirstDoseToday"] = df["FirstDose"].diff()
df["SecondDoseToday"] = df["SecondDose"].diff()
df["PfizerToday"] = df["Pfizer"].diff()
df["AstraZenecaToday"] = df["AstraZeneca"].diff()
df["ModernaToday"] = df["Moderna"].diff()

df["Doses7DayAverage"] = df["DosesToday"].rolling(7).sum()

# Converting time stamp to a to datetime e.g. 2020/03/22 00:00:0
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='%Y/%m/%d %H:%M:%S')

# Get doeses administered by week
df2 = df.groupby(df['TimeStamp'].dt.strftime('%W'))["DosesToday"].sum().reset_index(name ='Doses')

# Bar Chart - Doses Administered By Week
plt.bar(df2["TimeStamp"], df2["Doses"])
plt.xlabel('Week')
plt.ylabel('Doses')
plt.title('Doses Administered By Week')
plt.axhline(y=100000)
plt.show()

# Bar Chart - Doses Administered Last 7 Days
plt.bar(df["TimeStamp"], df["Doses7DayAverage"])
plt.xlabel('Date')
plt.ylabel('Doses')
plt.title('Doses Administered Roling 7 Day Roling Average')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.gcf().autofmt_xdate()
plt.axhline(y=80000)
plt.axhline(y=90000)
plt.axhline(y=100000)
plt.show()

# Bar Chart - Doses By Day
plt.bar(df["TimeStamp"], df["DosesToday"])
plt.xlabel('Date')
plt.ylabel('Doses')
plt.title('Doses Administered By Day')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.gcf().autofmt_xdate()
plt.show()
