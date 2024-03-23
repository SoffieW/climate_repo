import pandas as pd
import os
import tensorflow as tf
import csv
def import_data(file_name):
    '''
    import processed data as a series object.
    Args:
    file_name (str): name of csv file in data/processed directory
    Returns: 
    Series object 
    '''
    path_to_processed_data = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'processed', file_name+'.csv')
    data = pd.read_csv(path_to_processed_data, index_col = None)
    s = data[data.columns[0]]
    return s


def evaluate_preds(y_true, y_pred):
  '''
  calulates key error metrics for model
  *args:
  y_true: test values
  y_pred: model predictions
  '''
  # Make sure float32 (for metric calculations)
  y_true = tf.cast(y_true, dtype=tf.float32)
  y_pred = tf.cast(y_pred, dtype=tf.float32)

  # Calculate various metrics
  mae = tf.keras.metrics.mean_absolute_error(y_true, y_pred)
  mse = tf.keras.metrics.mean_squared_error(y_true, y_pred) # puts and emphasis on outliers (all errors get squared)
  rmse = tf.sqrt(mse)
  mape = tf.keras.metrics.mean_absolute_percentage_error(y_true, y_pred)
  return {"mae": mae.numpy(),
          "mse": mse.numpy(),
          "rmse": rmse.numpy(),
          "mape": mape.numpy()}



def write_dict_to_csv(dictionary, filepath):
# Open a csv file for writing
  with open(filepath, "w", newline="") as fp:
      # Create a writer object
      writer = csv.DictWriter(fp, fieldnames=dictionary.keys())

    # Write the header row
      writer.writeheader()

    # Write the data rows
      writer.writerow(dictionary)
      print('Done writing dict to a csv file')