import pandas as pd
import os
os.makedirs("data/clean", exist_ok=True)

df = pd.read_csv('data/raw/events.csv')
df = df.dropna()
df = df.loc[(df['event_type'].isin(['login', 'scroll', 'purchase', 'view', 'click'])) & (df['duration_seconds'] > 0)]
df['duration_seconds'] = df['duration_seconds'].astype(int)
df['timestamp'] = pd.to_datetime(df["timestamp"], format="mixed").dt.strftime('%Y-%m-%dT%H:%M:%S')

df.to_csv('data/clean/events.csv', index=False)