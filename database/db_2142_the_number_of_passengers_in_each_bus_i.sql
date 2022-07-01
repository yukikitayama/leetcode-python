select
  bus_id,
  -- count() returns 0 if none of passenger_id are joined and null
  count(distinct d.passenger_id) as passengers_cnt
from
  buses as c
left join (
-- Find arrival_times of bus that each user used
select
  b.passenger_id,
  -- b.arrival_time,
  min(a.arrival_time) as min_arrival_time
from
  buses as a,
  passengers as b
where
  b.arrival_time <= a.arrival_time
group by
  1
) as d
on
  c.arrival_time = d.min_arrival_time
group by
  1

;
