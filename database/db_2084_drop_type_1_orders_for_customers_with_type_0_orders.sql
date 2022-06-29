with cte as (
-- Find customer_ids which have at least one order of type 0
select
  distinct customer_id
from
  orders
where
  order_type = 0)

-- Get data of customers who didn't make type 0 orders so can have order_type 1
select
  *
from
  orders
where
  customer_id not in (
    select
      customer_id
    from
      cte
  )

union all

-- Get data of customers who ordered type 0 so only return type 0 data
select
  *
from
  orders
where
  customer_id in (
    select
      customer_id
    from
      cte
  )
  and order_type = 0

;