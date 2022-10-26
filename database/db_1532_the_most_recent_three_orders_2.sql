with cte as (
  select
    *,
    row_number() over(partition by customer_id order by order_date desc) as row_num
  from
    orders
)

select
  b.name as customer_name,
  a.customer_id,
  a.order_id,
  a.order_date
from
  cte as a
left join
  customers as b
on
  a.customer_id = b.customer_id
where
  a.row_num <= 3
order by
  1,
  2,
  4 desc
;