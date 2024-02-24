-- Write your PostgreSQL query statement below


select
  a.product_id,
  coalesce(round(sum(a.price * b.units)::decimal / sum(b.units), 2), 0) as average_price
from
  prices as a
left join
  unitssold as b
on
  a.product_id = b.product_id
  and b.purchase_date between a.start_date and a.end_date
group by
  1
;