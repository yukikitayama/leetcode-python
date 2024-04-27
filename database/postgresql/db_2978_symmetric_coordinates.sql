/*
(1, 2)
(2, 1)
mirrow at y = x
*/

-- Write your PostgreSQL query statement below
with cte as (
  select
    *,
    row_number() over() as id
  from
    coordinates
)


select
  distinct a.x,
  a.y
from
  cte as a
left join
  cte as b
on
  a.x = b.y
  and a.y = b.x
where
  a.id != b.id
  and a.x <= a.y
order by
  1,
  2
;
