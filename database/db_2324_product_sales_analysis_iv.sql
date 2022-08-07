-- Find total spent by user_id and product_id
with cte as (
select
  a.user_id,
  a.product_id,
  -- group by is applied to sum up quantities
  sum(a.quantity) * b.price as spent
from
  sales as a
left join
  product as b
on
  a.product_id = b.product_id
group by
  1,
  2
)

select
  user_id,
  product_id
-- Use subquery because we want to only have rnk is 1 and exclude rnk column in output
from (
select
  user_id,
  product_id,
  -- Items will have rnk 1 if spent most
  -- If multiple items, all have rnk 1
  dense_rank() over(partition by user_id order by spent desc) as rnk
from
  cte
) as c
where
  rnk = 1
;