-- Write your PostgreSQL query statement below

select
  distinct a.product_id,
  b.product_name
from
  sales as a
left join
  product as b
on
  a.product_id = b.product_id
where
  a.sale_date >= '2019-01-01'
  and a.sale_date <= '2019-03-31'
  and a.product_id not in (
    select product_id from sales where sale_date < '2019-01-01' or sale_date > '2019-03-31'
  )
;

