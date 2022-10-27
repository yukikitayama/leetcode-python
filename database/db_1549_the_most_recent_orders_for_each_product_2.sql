with cte as (
select
  b.product_name,
  a.product_id,
  a.order_id,
  a.order_date,
  rank() over(partition by a.product_id order by a.order_date desc) as rnk
from
  orders as a
left join
  products as b
on
  a.product_id = b.product_id
)

select
  product_name,
  product_id,
  order_id,
  order_date
from
  cte
where
  rnk = 1
order by
  1,
  2,
  3
;