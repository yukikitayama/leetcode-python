# Write your MySQL query statement below
with cte as (
  select
    customer_id,
    count(distinct product_key) as c
  from
    customer
  group by
    1
)

select
  customer_id
from
  cte
where
  c = (
    select count(distinct product_key) from product
  )