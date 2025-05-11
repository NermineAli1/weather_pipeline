# Weather Data Pipeline Project

This project is an end-to-end data pipeline that:

1. Extracts weather data from the [OpenWeatherMap API](https://openweathermap.org/api) 
2. Loads it into a PostgreSQL database via Docker
3. Transforms it with dbt
4. Visualizes average daily temperatures with Streamlit

---

## Project Structure
```text
weather_pipeline/
├── docker-compose.yml # PostgreSQL setup
├── .env # Environment variables (API key, DB config)
├── extract/
│ └── fetch_weather.py # Fetches weather data from API
├── load/
│ └── load_to_postgres.py # Loads weather data into PostgreSQL
├── dbt/
│ ├── dbt_project.yml # dbt config
│ └── models/
│ ├── staging/
│ │ └── stg_weather.sql
│ └── marts/
│ └── mart_avg_temp.sql
├── dashboard/
│ └── app.py
└── README.md
```
### Setup
1. Clone the repo bash
```
git clone https://github.com/your-username/weather_pipeline.git
cd weather_pipeline
```
2. Create .env

Create a .env file at the root with and replace the values with your own api key and postgres fields:
```
OPENWEATHER_API_KEY=your_api_key_here
POSTGRES_USER=weather_user
POSTGRES_PASSWORD=weather_pass
POSTGRES_DB=weather_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```
Note: You can get a free API key by signing up at [here](https://home.openweathermap.org/users/sign_up). 

Once signed up, create a key and paste it in your .env file and then you can test it in the by running the file ```python test/openweather_api_test.py```


3. Requirements
Install Python dependencies in a virtual environment:

```pip install -r requirements.txt```
### Next steps

Step 1: Launch PostgreSQL via Docker
```
docker-compose up -d
```

Step 2: Extract Weather Data
```
python extract/fetch_weather.py
```
Step 3: Load Data into PostgreSQL
```
python load/load_to_postgres.py
```
Note: You can only run this file since it contains the fetch_weather function and then it will load to the postgres database.

Step 4: Transform Data with dbt
```
cd dbt
dbt run
```
Note: You can run ```dbt debug``` to check before ```dbt run```.

Step 5: Launch the Dashboard
```
streamlit run dashboard/app.py
```




