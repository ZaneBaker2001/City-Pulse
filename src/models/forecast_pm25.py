from prophet import Prophet
import pandas as pd

def forecast_pm25(df):
    df = df.rename(columns={"datetime": "ds", "pm25": "y"})
    model = Prophet()
    model.fit(df[['ds', 'y']])
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    return forecast