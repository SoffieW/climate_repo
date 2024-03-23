# plot time series line graphs

import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import re
import matplotlib.dates as mdates
from datetime import datetime

def import_data(file_name):
    path_to_processed_data = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'processed', file_name+'.csv')
    data = pd.read_csv(path_to_processed_data, skiprows = 1, index_col = None)
    s = data[data.columns[0]]
    return s


def plot_time_series():
    X_train = pd.to_datetime(import_data('x_train'))
    y_train= import_data('y_train')
    X_val = pd.to_datetime(import_data('x_val'))
    y_val= import_data('y_val')
    X_test = pd.to_datetime(import_data('x_test'))
    y_test= import_data('y_test')

    plt.figure(figsize=(10, 6))
    plt.plot(X_train, y_train, marker='o', markersize = 1, linewidth = 0.5, color='b', label = 'Train')
    plt.plot(X_val, y_val, marker='o', markersize = 1, linewidth = 0.5, color='g', label = "Val")
    plt.plot(X_test, y_test, marker='o', markersize = 1, linewidth = 0.5, color='r', label = "Test")
    plt.legend()
    plt.title('Monthly Values Over Time')
    plt.xlabel('Year-Month')
    plt.ylabel('Temperature (\N{DEGREE SIGN}C)')

    plt.xticks(rotation=45, ha='right')  # Adjust rotation for better visibility
    plt.tight_layout()
    plt.show()



plot_time_series()
