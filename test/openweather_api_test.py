import requests
import os

response = requests.get(
    "https://api.stormglass.io/v2/weather/point",
    params={
        "lat": 58.7984,
        "lng": 17.8081,
        "params": "windSpeed",
    },
    headers={"Authorization": os.getenv("OPENWEATHER_API_KEY")},
)

# Do something with response data.
json_data = response.json()
print(json_data)
