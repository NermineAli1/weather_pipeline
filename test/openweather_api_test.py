import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={
        "q": "Paris",
        "appid": os.getenv("OPENWEATHER_API_KEY"),
        "units": "metric"
    }
)

print(response.status_code)
print(response.json())
