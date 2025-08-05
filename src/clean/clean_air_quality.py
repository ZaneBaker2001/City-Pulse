import pandas as pd

def clean_air_data(df):
    df = df.dropna()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df[df['pm25'] > 0]
    return df