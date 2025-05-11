with source as (
    select * from {{ source('public', 'raw_weather') }}
)

select
    city,
    temperature,
    humidity,
    weather,
    timestamp
from source
