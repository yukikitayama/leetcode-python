-- Use common table expression to make the final query look clean
-- instead of using subquery
with cte as (
  select
    city_id,
    day,
    degree,
    -- rank to find the earliest day among the max degrees in the same city multiple times
    dense_rank() over(partition by city_id order by degree desc, day) as rnk
  from
    weather
)

select
  city_id,
  day,
  degree
from
  cte
where
  rnk = 1
;