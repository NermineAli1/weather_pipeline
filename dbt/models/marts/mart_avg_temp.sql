{{ config(materialized='table') }}

SELECT
  city,
  DATE_TRUNC('day', timestamp) AS date,
  AVG(temperature) AS avg_temperature
FROM {{ ref('stg_weather') }}
GROUP BY city, DATE_TRUNC('day', timestamp)
