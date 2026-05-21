import pandas as pd

df = pd.read_csv('data/transformed/events.csv')
df['duration_minutes'] = df['duration_seconds'] / 60.
df['weekday'] = pd.to_datetime(df['timestamp']).dt.dayofweek

df.to_csv('data/features/events.csv')