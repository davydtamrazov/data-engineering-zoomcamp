~~~~sql
-- Create tables
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-411401.nytaxi.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-dtamrazov/green-taxi-2022/green_tripdata_2022-*.parquet']
);

CREATE OR REPLACE TABLE dtc-de-course-411401.nytaxi.green_tripdata
AS SELECT * FROM dtc-de-course-411401.nytaxi.external_green_tripdata;

-- Q1
SELECT COUNT (*) FROM dtc-de-course-411401.nytaxi.green_tripdata;

-- Q2
SELECT COUNT(DISTINCT PULocationID) FROM dtc-de-course-411401.nytaxi.external_green_tripdata;
SELECT COUNT(DISTINCT PULocationID) FROM dtc-de-course-411401.nytaxi.green_tripdata;

-- Q3
SELECT COUNT (*) FROM dtc-de-course-411401.nytaxi.green_tripdata WHERE fare_amount=0;

SELECT max(PULocationID), min(PULocationID) FROM dtc-de-course-411401.nytaxi.green_tripdata;

-- Q4
CREATE OR REPLACE TABLE dtc-de-course-411401.nytaxi.partitioned_clustered_green_tripdata
PARTITION BY
  DATE(lpep_pickup_datetime)
CLUSTER BY
  PULocationID
AS SELECT * FROM dtc-de-course-411401.nytaxi.external_green_tripdata;

-- Q5
SELECT DISTINCT PULocationID FROM dtc-de-course-411401.nytaxi.green_tripdata 
WHERE DATE(lpep_pickup_datetime) >= '2022-06-01' AND DATE(lpep_pickup_datetime) <= '2022-06-30';

SELECT DISTINCT PULocationID FROM dtc-de-course-411401.nytaxi.partitioned_clustered_green_tripdata 
WHERE DATE(lpep_pickup_datetime) >= '2022-06-01' AND DATE(lpep_pickup_datetime) <= '2022-06-30';
~~~~