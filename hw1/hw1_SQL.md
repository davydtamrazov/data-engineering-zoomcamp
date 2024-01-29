### Question #2

~~~~sql
SELECT * FROM public.yellow_taxi_trips
	WHERE lpep_pickup_datetime >= '2019-09-18 00:00'
	AND lpep_pickup_datetime < '2019-09-19 00:00'
	AND lpep_dropoff_datetime >= '2019-09-18 00:00'
	AND lpep_dropoff_datetime < '2019-09-19 00:00'
	ORDER BY lpep_pickup_datetime ASC
~~~~

### Question #3

~~~~sql
SELECT * FROM public.yellow_taxi_trips
	ORDER BY trip_distance DESC
~~~~

### Question #4

~~~~sql
SELECT z."Borough", SUM(yt.total_amount) sumtotal
	FROM yellow_taxi_trips yt
	JOIN zones z
	ON yt."PULocationID" = z."LocationID"
	WHERE lpep_pickup_datetime >= '2019-09-18 00:00'
	AND lpep_pickup_datetime < '2019-09-19 00:00'
	GROUP BY z."Borough"
~~~~

### Question #5

~~~~sql
SELECT pul."Zone" as pickup_zone, 
	   dol."Zone" as drop_zone, 
	   yt.tip_amount
	FROM yellow_taxi_trips yt
	LEFT JOIN zones pul 
		ON yt."PULocationID" = pul."LocationID"
	LEFT JOIN zones dol 
		ON yt."DOLocationID" = dol."LocationID"
	WHERE yt.lpep_pickup_datetime >= '2019-09-01 00:00'
	AND yt.lpep_pickup_datetime < '2019-09-30 23:59'
	AND pul."Zone" = 'Astoria'
	ORDER BY yt.tip_amount DESC
~~~~

