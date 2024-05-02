/*
booked_cnt
  min(capacity, count of passenger_id by flight id)
waitlist_cnt
  max(0, count of passenger id by flight id - capacity)
*/

-- Write your PostgreSQL query statement below
with cte as (
  select
    flight_id,
    count(distinct passenger_id) as num_passenger
  from
    passengers
  group by
    1
)

select
  a.flight_id,
  least(a.capacity, coalesce(b.num_passenger, 0)) as booked_cnt,
  greatest(0, coalesce(b.num_passenger, 0) - a.capacity) as waitlist_cnt
from
  flights as a
left join
  cte as b
on
  a.flight_id = b.flight_id
order by
  1
;
