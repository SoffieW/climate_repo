# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import os


def import_raw_file():
    path_to_raw_file = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'raw', 'global_mean_monthly_temps.csv')
    df = pd.read_csv(path_to_raw_file, skiprows = 1)
    return df
    
def separate_datasets(df):
    # separate seasonal and month columns into own datasets
    df_main = df[df.columns[:-6]]
    df_seasonal = df.iloc[:,[0,-6,-5,-4,-3,-2,-1]]
    return df_main, df_seasonal


def create_time_series(df):
    '''
    Pivot the main dataframe into time-series format
    '''

    # Melt the DataFrame to convert it to long format
    df_melted = pd.melt(df, id_vars='Year', var_name='Month', value_name='Value')

    # Combine 'Year' and 'Month' columns to create a 'year-month' column
    df_melted['Year-Month'] = df_melted['Year'].astype(str) + '-' + df_melted['Month']

    # Convert 'Year-Month' column to datetime
    df_melted['Year-Month'] = pd.to_datetime(df_melted['Year-Month'], format='%Y-%b')

    # Drop unnecessary columns
    df_pivoted = df_melted[['Year-Month', 'Value']]

    # Replace non-numeric values with NaN
    copied_col = df_pivoted['Value'].copy()

    # Use .loc for both operations to avoid SettingWithCopyWarning
    df_pivoted = df_pivoted.drop('Value', axis=1)
    df_pivoted.loc[:, 'Value'] = copied_col.apply(pd.to_numeric, errors='coerce')

    # Sort the DataFrame by 'Year-Month'
    df_time_series = df_pivoted.sort_values('Year-Month')

    # Return the pivoted DataFrame
    return df_time_series


def split_time_series(df):
    '''
    Splits time series dataset into train, val and test
    '''
    split_1 = int(0.8*len(df))
    split_2 = int(0.9*len(df))

    X_train = df[:split_1]["Year-Month"]
    X_val = df[split_1:split_2]["Year-Month"]
    X_test = df[split_2:]["Year-Month"]
    y_train = df[:split_1]["Value"]
    y_val = df[split_1:split_2]["Value"]
    y_test = df[split_2:]["Value"]

    return X_train, X_test, X_val, y_train, y_test, y_val

def interims_to_csv(df, string_name):
    interim_path = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'interim')
    df.to_csv(interim_path + "\\" + string_name + '.csv')

def splits_to_csv(split_name, string_name):
    '''
    outputs the train, test, val dimensions to separate csvs
    '''
    output_filepath = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'processed')
    output_filepath = output_filepath + "\\" + string_name + '.csv'
    split_name.to_csv(output_filepath)

def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    df = import_raw_file()
    separated_dfs = separate_datasets(df)
    df_main = separated_dfs[0]
    df_seasonal = separated_dfs[1]
    df_main = create_time_series(df_main)
    X_train, X_test, X_val, y_train, y_test, y_val  = split_time_series(df_main)
    splits_to_csv(X_train, "x_train")
    splits_to_csv(y_train, "y_train")
    splits_to_csv(X_test, "x_test")
    splits_to_csv(y_test, "y_test")
    splits_to_csv(X_val, "x_val")
    splits_to_csv(y_val, "y_val")
    interims_to_csv(df_main, "df_main")
    interims_to_csv(df_seasonal, "df_seasonal")

    
    
if __name__ == '__main__':
    main()

