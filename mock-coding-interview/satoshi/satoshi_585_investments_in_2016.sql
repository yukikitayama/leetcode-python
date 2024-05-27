# Write your MySQL query statement below

with cte as (
  select
    tiv_2015,
    count(*) as num_tiv
  from
    insurance
  group by
    1
),

cte2 as (
  select
    lat,
    lon,
    count(*) as num_loc
  from
    insurance
  group by
    1,
    2
)

select
  round(sum(tiv_2016), 2) as tiv_2016
from
  insurance
where
  tiv_2015 in (
    select tiv_2015 from cte where num_tiv > 1
  )
  and (lat, lon) in (
    select lat, lon from cte2 where num_loc = 1
  )
;
