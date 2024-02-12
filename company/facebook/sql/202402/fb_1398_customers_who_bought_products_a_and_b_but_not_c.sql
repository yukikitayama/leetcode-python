-- Write your PostgreSQL query statement below

with

a_buyer as (
  select
    customer_id
  from
    orders
  where
    product_name = 'A'
),

b_buyer as (
  select
    customer_id
  from
    orders
  where
    product_name = 'B'
),

c_buyer as (
  select
    customer_id
  from
    orders
  where
    product_name = 'C'
)

select
  customer_id,
  customer_name
from
  customers
where
  customer_id in (
    select * from a_buyer
  )
  and customer_id in (
    select * from b_buyer
  )
  and customer_id not in (
    select * from c_buyer
  )
order by
  1
;

