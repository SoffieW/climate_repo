from functions import import_data
from functions import evaluate_preds
from functions import write_dict_to_csv
import os
import pandas as pd
import csv
# Create a naïve forecast

y_test = import_data('y_test')
naive_forecast = y_test[:-1] # Naïve forecast equals every value excluding the last value
print(len(y_test[1:]))
print(len(naive_forecast))
model_name = "naive"
output_filepath = os.path.join(os.getcwd(), os.pardir,os.pardir, 'models', model_name)

if not os.path.exists(output_filepath):
    os.makedirs(output_filepath)


naive_forecast.to_csv(output_filepath + '\\naive_forecast.csv', index = False)


naive_results = evaluate_preds(y_test[1:], naive_forecast)


results_filepath = output_filepath + '\\results.csv'

write_dict_to_csv(naive_results, results_filepath)