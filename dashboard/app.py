import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Weather Dashboard")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT")
)

# Load data from mart
query = "SELECT * FROM mart_avg_temp ORDER BY date"
df = pd.read_sql(query, conn)

# Show city dropdown
cities = df["city"].unique()
selected_city = st.selectbox("Select a city", cities)

# Filter data by selected city
filtered_df = df[df["city"] == selected_city]

# Plot
st.line_chart(filtered_df.set_index("date")["avg_temperature"])

conn.close()
