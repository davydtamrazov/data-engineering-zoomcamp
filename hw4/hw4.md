
**fact_fhv\_trip.sql**

~~~~sql
{{ config(materialized='table') }}

with fhv_data as (
    select * from {{ ref("stg_fhv_tripdata")}}
),

dim_zones as (
    select * from {{ ref("dim_zones")}}
    where borough != 'Unknown'
)

select 
    fhv_data.*,
    pickup_zone.Zone as pickup_zone_name,
    dropoff_zone.Zone as dropoff_zone_name
from fhv_data
inner join dim_zones as pickup_zone
on fhv_data.PULocationID = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on fhv_data.DOLocationID = dropoff_zone.locationid


~~~~

**stg_fhv\_tripdata.sql**

~~~~sql
{{ config(materialized='view') }}

select * from {{ source("staging", "fhv_tripdata") }}
where EXTRACT(year from pickup_datetime) = 2019

{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
~~~~

