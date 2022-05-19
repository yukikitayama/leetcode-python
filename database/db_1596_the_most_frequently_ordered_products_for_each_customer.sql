with cte as (
select
  customer_id,
  product_id,
  count(product_id) as cnt
from
  orders
group by
  1,
  2
)

select
  a.customer_id,
  a.product_id,
  b.product_name
from
  cte as a
join
  products as b
on
  a.product_id = b.product_id
where
  a.cnt in (
    select
      max(cnt)
    from
      cte as c
    where
      a.customer_id = c.customer_id
  )
;
