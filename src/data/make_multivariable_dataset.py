import pandas as pd
import os


def make_multivar_dataset():
    '''
    combines data from multiple sources into one dataframe for multivariate analysis. 
    Exports csv file to /data/interim
    '''
    temps_path = os.path.join(os.getcwd(), os.pardir, os.pardir,"data", "interim", "df_seasonal.csv")
    elninonina_path = os.path.join(os.getcwd(), os.pardir, os.pardir, "data", "external", "elnino_lanina.csv")

    temps_df = pd.read_csv(temps_path)
    temps_df = temps_df[['Year', 'DJF', 'MAM', 'JJA', 'SON']]
    nn_df = pd.read_csv(elninonina_path)
    nn_df = nn_df[['Year', 'DJF', 'MAM', 'JJA', 'SON']]
    merged = pd.merge(temps_df, nn_df, on = "Year")
    output_path = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'interim', 'multivariable.csv')
    merged.to_csv(output_path, index = False)


if __name__ =='__main__':
    make_multivar_dataset()




