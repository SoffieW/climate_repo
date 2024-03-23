from functions import import_data
import os

# Create a naïve forecast
y_test = import_data('y_test')
naive_forecast = y_test[:-1] # Naïve forecast equals every value excluding the last value

output_filepath = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'predictions')
naive_forecast.to_csv(output_filepath + '\\naive_forecast.csv', index = False)
