import sys
import os
import psycopg2
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract.fetch_weather import fetch_weather

load_dotenv()

# Connexion à PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT")
)

cur = conn.cursor()

# Créer la table si elle n'existe pas
cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_weather (
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        weather TEXT,
        timestamp TIMESTAMP
    );
""")

# Récupérer les données météo et insérer dans la base
data = fetch_weather()

cur.execute("""
    INSERT INTO raw_weather (city, temperature, humidity, weather, timestamp)
    VALUES (%s, %s, %s, %s, to_timestamp(%s))
""", (data["city"], data["temperature"], data["humidity"], data["weather"], data["timestamp"]))

conn.commit()
cur.close()
conn.close()

print("Succès!")
