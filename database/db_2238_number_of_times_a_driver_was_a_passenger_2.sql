with cte as (
  select
    passenger_id as driver_id,
    count(*) as cnt
  from
    rides
  group by
    1
)

select
  distinct a.driver_id,
  ifnull(b.cnt, 0) as cnt
from
  rides as a
left join
  cte as b
on
  a.driver_id = b.driver_id
;
