from make_dataset import import_raw_file
from make_dataset import separate_datasets
from make_dataset import create_time_series
import os
#path_to_raw_file = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'raw', 'global_mean_monthly_temps.csv')
df = import_raw_file()

print(df)

df_main, df_seasonal =separate_datasets(df)

df_main = create_time_series(df_main)

print(df_main.dropna())
print(df_main.tail(12))