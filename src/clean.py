import pandas as pd

df = pd.read_csv('data/raw/events.csv')
df = df.dropna()
df = df.loc[(df['event_type'].isin(['login', 'scroll', 'purchase', 'view', 'click'])) & (df['duration_seconds'] > 0)]
df['timestamp'] = pd.to_datetime(df["timestamp"], format="mixed")

df.to_csv('data/clean/events.csv')