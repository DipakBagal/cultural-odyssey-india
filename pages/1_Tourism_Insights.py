import streamlit as st
import pandas as pd
import altair as alt
import snowflake.connector

st.title("📊 Tourism Analytics")

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
df['YEAR'] = pd.to_datetime(df['YEAR'])

st.altair_chart(alt.Chart(df).mark_line().encode(
    x='YEAR:T',
    y='FOREIGN_TOURIST_ARRIVALS:Q'
).properties(title="Foreign Tourist Arrivals Over Time"), use_container_width=True)