with
-- Change flights table into a vertical format for conveniece to group by query
cte1 as (
select
  departure_airport as airport,
  flights_count
from
  flights
union all
select
  arrival_airport as airport,
  flights_count
from
  flights
),

-- Compute total number of flights by airport
cte2 as (
  select
    airport,
    sum(flights_count) as total_flights_count
  from
    cte1
  group by
    airport
)

# select * from cte2;

-- Get airport IDs which have most traffic
select
  airport as airport_id
from
  cte2
where
  total_flights_count = (
    -- Identify the count of the most traffic
    select
      max(total_flights_count)
    from
      cte2
  )
;