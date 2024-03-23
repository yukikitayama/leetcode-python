# Write your MySQL query statement below
with cte as (
  select
    tiv_2015,
    if(count(*) > 1, 1, 0) as c1
  from
    insurance
  group by
    1
),

cte2 as (
  select
    lat,
    lon,
    if(count(*) > 1, 0, 1) as c2
  from
    insurance
  group by
    1,
    2
)

-- select * from cte;
-- select * from cte2;

select
  round(sum(a.tiv_2016), 2) as tiv_2016
from
  insurance as a
left join
  cte as b
on
  a.tiv_2015 = b.tiv_2015
left join
  cte2 as c
on
  a.lat = c.lat
  and a.lon = c.lon
where
  c1 = 1
  and c2 = 1
;