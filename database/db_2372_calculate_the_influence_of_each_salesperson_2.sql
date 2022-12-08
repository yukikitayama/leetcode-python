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
  b.salesperson_id
)

-- select * from cte;

select
  a.salesperson_id,
  a.name,
  ifnull(b.total, 0) as total
from
  salesperson as a
left join
  cte as b
on
  a.salesperson_id = b.salesperson_id
;