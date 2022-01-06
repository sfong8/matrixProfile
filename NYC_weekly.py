
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

m = 24*7*30
mp = stumpy.stump(taxi_df['value'], m=m)

# motif_idx = np.argsort(mp[:, 0])[0]
# print(f"The motif is located at index {motif_idx}")
# nearest_neighbor_idx = mp[motif_idx, 1]
# print(f"The nearest neighbor is located at index {nearest_neighbor_idx}")
# fig, axs = plt.subplots(2, sharex=True, gridspec_kw={'hspace': 0})
# plt.suptitle('Motif (Pattern) Discovery', fontsize='30')
# axs[0].plot(taxi_df['value'].values)
# axs[0].set_ylabel('value', fontsize='20')
# rect = Rectangle((motif_idx, 0), m, 40, facecolor='lightgrey')
# axs[0].add_patch(rect)
# rect = Rectangle((nearest_neighbor_idx, 0), m, 40, facecolor='lightgrey')
# axs[0].add_patch(rect)
# axs[1].set_xlabel('Time', fontsize ='20')
# axs[1].set_ylabel('Matrix Profile', fontsize='20')
# axs[1].axvline(x=motif_idx, linestyle="dashed")
# axs[1].axvline(x=nearest_neighbor_idx, linestyle="dashed")
# axs[1].plot(mp[:, 0])
# plt.show()



discord_idx = np.argsort(mp[:, 0])[-1]
print(f"The discord is located at index {discord_idx}")
nearest_neighbor_distance = mp[discord_idx, 0]
print(f"The nearest neighbor subsequence to this discord is {nearest_neighbor_distance} units away")
fig, axs = plt.subplots(2, sharex=True, gridspec_kw={'hspace': 0})
plt.suptitle('Discord (Anomaly/Novelty) Discovery', fontsize='30')

axs[0].plot(taxi_df['value'].values)
axs[0].set_ylabel('value', fontsize='20')
rect = Rectangle((discord_idx, 0), m, 40, facecolor='lightgrey')
axs[0].add_patch(rect)
axs[1].set_xlabel('Time', fontsize ='20')
axs[1].set_ylabel('Matrix Profile', fontsize='20')
axs[1].axvline(x=discord_idx, linestyle="dashed")
axs[1].plot(mp[:, 0])
plt.show()