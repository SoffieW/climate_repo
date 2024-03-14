import requests
from pathlib import Path
import os


def main():
    path = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'raw')
    print(path)

    url='https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv'

    response = requests.get(url)
    with open(os.path.join(path, "global_mean_monthly_temps.csv"), 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    main()