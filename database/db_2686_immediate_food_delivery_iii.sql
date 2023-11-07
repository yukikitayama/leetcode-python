with cte as (
  select
    order_date,
    if(order_date = customer_pref_delivery_date, 1, 0) as immediate
  from
    delivery
)

select
  order_date,
  round(avg(immediate) * 100, 2) as immediate_percentage
from
  cte
group by
  1
order by
  1
;