# utils/forecast.py

import pandas as pd
from prophet import Prophet

def prepare_prophet_data(df):
    df_prophet = df[['date', 'visitors']].rename(columns={'date': 'ds', 'visitors': 'y'})
    return df_prophet

def forecast_visitors(df, periods=12):
    prophet_df = prepare_prophet_data(df)
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]