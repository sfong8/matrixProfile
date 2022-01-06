import pandas as pd
from matplotlib import pyplot as plt

base_url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-{}.csv'


def month_generator():
    for i in range(1, 13):
        month = str(i)

        if len(month) == 1:
            month = '0{}'.format(month)

        yield month


# each month of data we resample it here
# note that some dates are not even in 2018 or the same month, those are thrown away
def resample_hourly(df,month):
    df = df.rename(columns={'tpep_pickup_datetime': 'pickup_datetime'})
    df['year'] = df['pickup_datetime'].apply(lambda s: s.split('-')[0])
    df['month'] = df['pickup_datetime'].apply(lambda s: s.split('-')[1])
    year_month_filter = (df['year'] == '2020') & (df['month'] == month)
    df = df[year_month_filter].copy()
    df = df.drop(columns=['year', 'month'])
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
    df = df.set_index('pickup_datetime').sort_index()

    return df.resample('H').sum()


# read all csvs and concatenate them
dfs = []

# limit data to pickup date and time and the passenger count
# the data sets are fairly large ~1GB each and we only care to aggregate
columns = ['tpep_pickup_datetime', 'passenger_count']
import os

for file in os.listdir('./data/'):
    print(file)
    # url = base_url.format(month)
    # print(month)
    if file.endswith('csv'):
        df = pd.read_csv(fr'./data/{file}')
        month = file[21:23]
        df = df[['tpep_pickup_datetime', 'passenger_count']]
        hourly_df = resample_hourly(df,month)
        dfs.append(hourly_df)

df = pd.concat(dfs)

df.to_csv('nyc_yellowcab_passenger_hourly_count.csv')