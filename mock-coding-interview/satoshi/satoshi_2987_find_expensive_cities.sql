# Write your MySQL query statement below
with cte as (
  select
    city,
    avg(price) as city_price
  from
    listings
  group by
    city
)

select
  city
from
  cte
where
  city_price > (
    select avg(price) from listings
  )
order by
  1
;
