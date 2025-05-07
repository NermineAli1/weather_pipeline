import psycopg2
from extract.fetch_weather import fetch_weather
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT")
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_weather (
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        weather TEXT,
        timestamp TIMESTAMP
    );
""")

data = fetch_weather()
cur.execute("""
    INSERT INTO raw_weather (city, temperature, humidity, weather, timestamp)
    VALUES (%s, %s, %s, %s, to_timestamp(%s))
""", (data["city"], data["temperature"], data["humidity"], data["weather"], data["timestamp"]))

conn.commit()
cur.close()
conn.close()
