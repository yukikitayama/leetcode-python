-- Write your PostgreSQL query statement below
with cte as (
  select
    customer_id,
    order_id,
    order_date,
    rank() over(
      partition by customer_id
      order by order_date desc
    ) as rank
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
join
  customers as b
on
  a.customer_id = b.customer_id
where
  a.rank <= 3
order by
  1,
  2,
  4 desc
;
