-- Total prices by customer_id and year
with cte as (
  select
    customer_id,
    year(order_date) as order_year,
    sum(price) as total
  from
    orders
  group by
    customer_id,
    year(order_date)
)

-- select * from cte;

select
  a.customer_id
from
  cte as a
left join
  cte as b
on
  a.customer_id = b.customer_id
  -- Strictly increasing yearly
  and a.order_year + 1 = b.order_year
  and a.total < b.total
group by
  a.customer_id
having
  -- +1 because the last year has not been joined and null
  count(a.customer_id) = count(b.customer_id) + 1
;