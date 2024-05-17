-- Write your PostgreSQL query statement below

with cte as (
  select
    a.user_id,
    a.product_id,
    rank() over(
      partition by a.user_id
      order by sum(a.quantity * b.price) desc
    ) as rank
  from
    sales as a
  left join
    product as b
  on
    a.product_id = b.product_id
  group by
    a.user_id,
    a.product_id
)

select
  user_id,
  product_id
from
  cte
where
  rank = 1
;