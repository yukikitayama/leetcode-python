--select
--  round(
--    sum(if(a.order_date = a.customer_pref_delivery_date, 1, 0)) / count(*) * 100,
--    2
--  ) as immediate_percentage
--from
--  delivery as a
--inner join (
--select
--  customer_id,
--  min(order_date) as first_order_date
--from
--  delivery
--group by
--  customer_id
--) as b
--on
--  a.customer_id = b.customer_id
--  and a.order_date = b.first_order_date
--;


select
  round(
    sum(if(a.order_date = a.customer_pref_delivery_date, 1, 0)) / count(*) * 100,
    2
  ) as immediate_percentage
from
  delivery as a
where
  (a.customer_id, a.order_date) in (
select
  customer_id,
  min(order_date) as first_order_date
from
  delivery
group by
  customer_id
  )
;
