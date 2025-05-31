import streamlit as st
import pandas as pd
import snowflake.connector

st.title("🎉 Festival Explorer")

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
df = pd.read_sql("SELECT * FROM STATE_FESTIVALS", conn)

state = st.selectbox("Select State", df['STATE'].unique())
filtered = df[df['STATE'] == state]

for _, row in filtered.iterrows():
    st.subheader(f"{row['FESTIVALS']} in {row['STATE']}")
    st.image(f"https://source.unsplash.com/600x300/?{row['STATE']},festival", use_column_width=True)
    st.write(f"💰 Sanctioned: ₹{row['SANCTIONED_AMOUNT']} Lakh")