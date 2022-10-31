with
cte1 as (
  select
    customer_id,
    product_id,
    count(*) as num_order
  from
    orders
  group by
    1,
    2
),

cte2 as (
  select
    *,
    rank() over(partition by customer_id order by num_order desc) as rnk
  from
    cte1
)

select
  a.customer_id,
  a.product_id,
  b.product_name
from
  cte2 as a
left join
  products as b
on
  a.product_id = b.product_id
where
  rnk = 1
;

--with cte as (
--  select
--    *,
--    rank() over(
--      partition by customer_id
--      order by count(product_id) desc
--    ) as rnk
--  from
--    orders
--  group by
--    customer_id,
--    product_id
--)
--
--select
--  a.customer_id,
--  a.product_id,
--  b.product_name
--from
--  cte as a
--left join
--  products as b
--on
--  a.product_id = b.product_id
--where
--  rnk = 1
--;

