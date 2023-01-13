import os
import pandas as pd

HISTORICAL_DATA='data/raw/apprenticeships/201920-July_totals-since-may-2010-and-2015.xlsx'

data = pd.read_excel(HISTORICAL_DATA, sheet_name='la_2010', skiprows=1, na_values='-')
geo_codes = pd.read_excel(HISTORICAL_DATA, sheet_name='geo_code_lookup', skiprows=4, usecols='D:E').dropna()

data = data[~data['Local Authority'].str.contains('Total')]
data = data.melt(id_vars=['Local Authority'])
data = data.merge(geo_codes, left_on='Local Authority', right_on='LA')

OUTPUT_DIR='data/working/apprenticeships/'
os.makedirs(OUTPUT_DIR, exist_ok=True)

pd.DataFrame({
  'la_code': data['LA Code'],
  'period': data['variable'],
  'value': data['value'],
}).to_csv(OUTPUT_DIR + 'historical.csv', index=False)


