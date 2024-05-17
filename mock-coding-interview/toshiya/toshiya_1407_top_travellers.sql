-- Write your PostgreSQL query statement below
with cte as (
  select
    a.name,
    a.id,
    coalesce(sum(b.distance), 0) as travelled_distance
  from
    users as a
  left join
    rides as b
  on
    a.id = b.user_id
  group by
    1,
    2
)

select
  name,
  travelled_distance
from
  cte
order by
  2 desc,
  1
;