# Write your MySQL query statement below
select
  a.product_id,
  b.product_name
from
  sales as a
left join
  product as b
on
  a.product_id = b.product_id
group by
  a.product_id
having
  min(a.sale_date) >= '2019-01-01'
  and max(a.sale_date) <= '2019-03-31'
;