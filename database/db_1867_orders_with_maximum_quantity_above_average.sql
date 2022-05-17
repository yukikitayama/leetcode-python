with cte as (
  select
    order_id,
    avg(quantity) as avg_quantity,
    max(quantity) as max_quantity
  from
    ordersdetails
  group by
    order_id
)

select
  order_id
from
  cte
where
  max_quantity > (
    select
      max(avg_quantity)
    from
      cte
  )
;
