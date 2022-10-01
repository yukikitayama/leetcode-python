with
-- Assign ranking about how much the price are recent by product
-- when the date is less than or equal to the date
cte1 as (
select
  product_id,
  new_price,
  change_date,
  row_number() over(partition by product_id order by change_date desc) as row_num
from
  products
where
  change_date <= '2019-08-16'
),

-- Find the latest price by product_id
cte2 as (
select
  product_id,
  new_price as price
from
  cte1
where
  row_num = 1
),

-- Manually creat price for the products which changed after the data
-- because these products are missed from the above CTEs
cte3 as (
  select
    product_id,
    10 as price
  from
    products
  group by
    1
  having
    min(change_date) > '2019-08-16'
)

-- Join both types of products as output
select
  *
from
  cte2
union
select
  *
from
  cte3
;