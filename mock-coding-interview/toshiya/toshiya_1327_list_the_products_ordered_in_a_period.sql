# Write your MySQL query statement below
select
  b.product_name,
  sum(a.unit) as unit
from
  orders as a
left join
  products as b
on
  a.product_id = b.product_id
where
  a.order_date >= '2020-02-01'
  and a.order_date < '2020-03-01'
group by
  1
having
  sum(a.unit) >= 100
;