with
cte as (
  select
    order_id,
    -- Maximum quantity of each order
    max(quantity) as max_quantity,
    -- Average quantity of each order
    avg(quantity) as avg_quantity
  from
    ordersdetails
  group by
    1
)

select
  order_id
from
  cte
where
  max_quantity > (
    select max(avg_quantity) from cte
  )
;
