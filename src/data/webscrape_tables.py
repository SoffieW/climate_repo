import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import os


# URL of the website
url = 'https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php'

    # Send a GET request to the URL
response = requests.get(url)

    # Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first table in the page
table = soup.find_all('table')[3]

    # Extract data from the table
data = []
for row in table.find_all('tr'):
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    if row_data:
        data.append(row_data)


table_data = []
for row in data[50:]:
    if 'Year' in row:
        continue
    table_data.append(row)


table_dataframe = pd.DataFrame(table_data)
table_dataframe.columns = data[49]
extraction_path = os.path.join(os.getcwd(), os.pardir,os.pardir, 'data', 'external', 'elnino_lanina.csv')
table_dataframe.to_csv(extraction_path)

