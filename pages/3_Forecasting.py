import streamlit as st
import pandas as pd
from prophet import Prophet
import snowflake.connector

st.title("🔮 Tourism Forecasting")

@st.cache_resource
def get_conn():
    return snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    warehouse=st.secrets["snowflake"]["warehouse"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"]
    )
conn = get_conn()

df = pd.read_sql("SELECT * FROM TOURISM_DATA", conn)
df = df[['YEAR', 'FOREIGN_TOURIST_ARRIVALS']].dropna()
df.columns = ['ds', 'y']
df['ds'] = pd.to_datetime(df['ds'])

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=5, freq='Y')
forecast = model.predict(future)

st.line_chart(forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']])