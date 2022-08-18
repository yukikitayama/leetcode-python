-- Precompute sum of customer payments by sales person
with cte as (
select
  b.salesperson_id,
  sum(a.price) as total
from
  sales as a
left join
  customer as b
on
  a.customer_id = b.customer_id
group by
  1
)

select
  c.salesperson_id,
  c.name,
  -- ifnull() because the problem requires us to return 0 if a sales person doesn't have any customers, so left join fails and it contains null.
  ifnull(d.total, 0) as total
from
  salesperson as c
left join
  cte as d
on
  c.salesperson_id = d.salesperson_id
;