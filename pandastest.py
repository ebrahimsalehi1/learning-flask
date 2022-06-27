import pandas as pd

df = pd.read_csv('data.csv', index_col=0, parse_dates=['IND_DAY']) 
df.to_csv('formatted-data.csv', date_format='%B %d, %Y')
