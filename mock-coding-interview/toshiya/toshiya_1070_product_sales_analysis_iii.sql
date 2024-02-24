-- Write your PostgreSQL query statement below

with cte as (
  select
    product_id,
    min(year) as first_year
  from
    sales
  group by
    1
)

select
  product_id,
  year as first_year,
  quantity,
  price
from
  sales
where
  (product_id, year) in (
    select product_id, first_year from cte
  )
;
