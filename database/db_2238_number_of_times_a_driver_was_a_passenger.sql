select
  a.driver_id,
  count(distinct b.ride_id) as cnt
from
  rides as a
left join
  rides as b
on
  a.driver_id = b.passenger_id
group by
  1
