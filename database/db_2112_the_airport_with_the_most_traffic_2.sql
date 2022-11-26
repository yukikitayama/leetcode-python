with
cte1 as (
  select
    departure_airport as airport_id,
    flights_count
  from
    flights
  union all
  select
    arrival_airport as airport_id,
    flights_count
  from
    flights
),
cte2 as (
  select
    airport_id,
    sum(flights_count) as total_flight
  from
    cte1
  group by
    1
)

select
  airport_id
from
  cte2
where
  total_flight = (
    select max(total_flight) from cte2
  )
;