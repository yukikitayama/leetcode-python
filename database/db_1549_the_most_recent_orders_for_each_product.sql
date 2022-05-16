select
  b.product_name,
  b.product_id,
  a.order_id,
  a.order_date
from
  orders as a
join
  products as b
on
  a.product_id = b.product_id
where
  (b.product_id, a.order_date) in (
select
  product_id,
  max(order_date) as order_date
from
  orders
group by
  product_id
  )
order by
  1,
  2,
  3
;