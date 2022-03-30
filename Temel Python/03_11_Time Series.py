# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
# import pandas_datareader as pddr
import seaborn

# %%
# Time stamp --> July 4th, 2015 at 07:00 am
from datetime import datetime

print(datetime(year=2015, month=7, day=4))

# %%
from dateutil import parser

date = parser.parse("4th of July, 2015")
print(date)

# %%
date.strftime('%A')
# %%
date.strftime('%a')
# %%
date.strftime('%w')
# %%
date.strftime('%d')
# %%
date.strftime('%b')
# %%
date.strftime('%B')
# %%
date.strftime('%m')
# %%
date.strftime('%y')
# %%
date.strftime('%Y')
# %%
date.strftime('%H')
# %%
date.strftime('%I')
# %% Day number x/365
date.strftime('%j')
# %% Week number
date.strftime('%U')
# %%
date.strftime('%m')

# %% Numpy encodes dates as 64-bit integers. More productive
date = np.array('2015-07-04', dtype=np.datetime64)
print(date)

# %%
date + np.arange(10)

# %% time indexed data
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data)

# %%
data['2014-07-04':'2015-07-04']

# %%
dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                        '2015-Jul-6', '07-07-2015', '20150708'])
print(dates)

# %%
print(dates[4] - dates[0])

# %%
print(pd.period_range('2015-07', periods=8, freq='M'))

# %% Seatle Bicycle Counts
url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv'
data = pd.read_csv(url, index_col='Date', parse_dates=True)
print(data)

# %%
data.columns = ['Total', 'East', 'West']

# %%
data.dropna().describe()

# %%
# %matplotlib inline
seaborn.set()
data['Total'].plot()
plt.title('Seattle Bicycle Usage', fontsize=16)
plt.ylabel('Hourly Bicycle Count', fontsize=12)
plt.xlabel('Date', fontsize=12)
plt.show()

# %% Too dense for daily plot
weekly = data.resample('W').sum()
weekly.plot(style=[':', '--', '-'])
plt.title('Seattle Bicycle Usage', fontsize=16)
plt.ylabel('Weekly bicycle count')
plt.xlabel('Date', fontsize=12)
plt.show()

# %%
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-'])
plt.show()

# %%
by_weekday = data.groupby(data.index.dayofweek).mean()
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
by_weekday.plot(style=[':', '--', '-'])
plt.show()
















