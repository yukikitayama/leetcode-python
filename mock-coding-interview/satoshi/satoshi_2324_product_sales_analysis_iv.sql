-- Write your PostgreSQL query statement below

with cte as (
  select
    a.user_id,
    a.product_id,
    a.quantity * b.price as spent
  from
    sales as a
  left join
    product as b
  on
    a.product_id = b.product_id
),

cte2 as (
  select
    user_id,
    product_id,
    sum(spent) as total_spent
  from
    cte
  group by
    1,
    2
),

cte3 as (
  select
    user_id,
    product_id,
    rank() over(
      partition by user_id
      order by total_spent desc
    ) as rank
  from
    cte2
)

-- select * from cte order by user_id, product_id;
-- select * from cte2 order by user_id, product_id;

select
  user_id,
  product_id
from
  cte3
where
  rank = 1
;