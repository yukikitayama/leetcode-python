with cte as (
select
  customer_id,
  min(order_date) as first_order_date
from
  delivery
group by
  1
)

select
  round(avg(if(order_date = customer_pref_delivery_date, 1, 0)) * 100, 2) as immediate_percentage
from
  delivery
where
  (customer_id, order_date) in (
    select * from cte
  )
;
