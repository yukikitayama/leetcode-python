with cte as (
  select
    distinct customer_id
  from
    orders
  where
    order_type = 0
)

select
  *
from
  orders
where
  (customer_id in (
    select * from cte
  )
  and order_type = 0)
  or customer_id not in (
    select * from cte
  )
;
