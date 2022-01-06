
import pandas as pd
import stumpy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.patches import Rectangle
import datetime as dt

plt.style.use('https://raw.githubusercontent.com/TDAmeritrade/stumpy/main/docs/stumpy.mplstyle')


taxi_df = pd.read_csv("nyc_yellowcab_passenger_hourly_count.csv")
taxi_df.columns = ['timestamp','value']
taxi_df=taxi_df.sort_values(by=['timestamp']).reset_index()
taxi_df['value'] = taxi_df['value'].astype(np.float64)
taxi_df['timestamp'] = pd.to_datetime(taxi_df['timestamp'])
taxi_df.head()

m = 24
mp = stumpy.stump(taxi_df['value'], m=m)
test = pd.DataFrame(mp)
y = test.sort_values(by = [0],ascending=False).head(5)


plt.suptitle('1-Day STUMP', fontsize='30')
plt.xlabel('Window Start', fontsize ='20')
plt.ylabel('Matrix Profile', fontsize='20')
plt.plot(taxi_df['timestamp'][:8761],mp[:, 0])

# plt.plot(575, 1.7, marker="v", markersize=15, color='b')
# plt.text(620, 1.6, 'Columbus Day', color="black", fontsize=20)
# plt.plot(1535, 3.7, marker="v", markersize=15, color='b')
# plt.text(1580, 3.6, 'Daylight Savings', color="black", fontsize=20)
# plt.plot(2700, 3.1, marker="v", markersize=15, color='b')
# plt.text(2745, 3.0, 'Thanksgiving', color="black", fontsize=20)
# plt.plot(30, .2, marker="^", markersize=15, color='b', fillstyle='none')
# plt.plot(363, .2, marker="^", markersize=15, color='b', fillstyle='none')
# plt.xticks(np.arange(0, 3553, (m*DAY_MULTIPLIER)/2), x_axis_labels)
# plt.xticks(rotation=75)
plt.minorticks_on()
plt.show()