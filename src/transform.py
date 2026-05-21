import pandas as pd

df = pd.read_csv('data/clean/events.csv')
df['date'] = pd.to_datetime(df['timestamp']).dt.date

df.to_csv('data/transformed/events.csv')