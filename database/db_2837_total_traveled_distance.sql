with total_distance as (
  select
    user_id,
    sum(distance) as total_distance
  from
    rides
  group by
    1
)

select
  a.user_id,
  a.name,
  ifnull(b.total_distance, 0) as 'traveled distance'
from
  users as a
left join
  total_distance as b
on
  a.user_id = b.user_id
order by
  1
;