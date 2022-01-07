import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import matrixprofile as mp
plt.style.use('https://raw.githubusercontent.com/TDAmeritrade/stumpy/main/docs/stumpy.mplstyle')


df = pd.read_csv("nyc_yellowcab_passenger_hourly_count.csv")
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])


df = df.set_index('pickup_datetime').sort_index()

# taxi_df.columns = ['timestamp','value']
# taxi_df=taxi_df.sort_values(by=['timestamp']).reset_index()
# taxi_df['value'] = taxi_df['value'].astype(np.float64)
# taxi_df['timestamp'] = pd.to_datetime(taxi_df['timestamp'])
# taxi_df.head()
windows = [
    ('24 Hours', 24),
    ('7 Days', 7 * 24),
    ('30 Days', 30 * 24),
]

profiles = {}

for label, window_size in windows:
    profile = mp.compute(df['passenger_count'].values, window_size)
    key = '{} Profile'.format(label)
    profiles[key] = profile


# #Plot the signal data
# fig, axes = plt.subplots(3,1,sharex=True,figsize=(15,10))
#
# for ax_idx, window in enumerate(windows):
#     key = '{} Profile'.format(window[0])
#     profile = profiles[key]
#     axes[ax_idx].plot(profile['mp'])
#     axes[ax_idx].set_title(key)
#
# plt.xlabel('Pickup Datetime')
# plt.tight_layout()
# plt.show()

# label = '24 Hours'
# key = 24
# key = '{} Profile'.format(label)
# profiles[key] = mp.discover.discords(profiles[key], k=5)
#
# window_size = profiles[key]['w']
# mp_adjusted = np.append(profiles[key]['mp'], np.zeros(window_size - 1) + np.nan)
#
# plt.figure(figsize=(15, 7))
# ax = plt.plot(df.index.values, mp_adjusted)
# plt.title(key)
#
# for start_index in profiles[key]['discords']:
#     x = df.index.values[start_index:start_index + window_size]
#     y = mp_adjusted[start_index:start_index + window_size]
#     plt.plot(x, y, c='r')
#
# plt.show()
#
# for label, window_size in windows:
#     key = '{} Profile'.format(label)
#     profiles[key] = mp.discover.discords(profiles[key], k=5)
#
#     window_size = profiles[key]['w']
#     mp_adjusted = np.append(profiles[key]['mp'], np.zeros(window_size - 1) + np.nan)
#
#     plt.figure(figsize=(15, 7))
#     ax = plt.plot(df.index.values, mp_adjusted)
#     plt.title(key)
#
#     for start_index in profiles[key]['discords']:
#         x = df.index.values[start_index:start_index + window_size]
#         y = mp_adjusted[start_index:start_index + window_size]
#         plt.plot(x, y, c='r')
#
#     plt.show()
#

key = '24 Hours Profile'
profiles[key] = mp.discover.discords(profiles[key], k=5)
profile = profiles[key]

window_size = profile['w']
mp_adjusted = np.append(profile['mp'], np.zeros(window_size - 1) + np.nan)
df['24 Hours Profile'] = mp_adjusted

ax = df[key].plot(title='24 Hour Matrix Profile', figsize=(15,5))

# for discord in profile['discords']:
#     df.iloc[discord:discord+window_size][key].plot(ax=ax, c='r', lw='2')

# df.iloc[profile['discords']][key].plot(kind='line', marker='*', c='black', markersize=8, ax=ax, lw=0)
plt.text('2020-01-01', 2.5, '1', c='red',fontsize=12, weight='bold')
plt.text('2020-01-25', 1.5, '2', c='red',fontsize=12, weight='bold')
plt.text('2020-02-01', 2, '3', c='red',fontsize=12, weight='bold')
plt.text('2020-03-08', 2.7, '4', c='red',fontsize=12, weight='bold')
plt.text('2020-10-31', 2.7, '5', c='red',fontsize=12, weight='bold')
# plt.text('03-14-2018', 2.675, 'Daylight Savings Begin', c='black')
plt.xlabel('Pickup Datetime')
plt.tight_layout()
plt.show()