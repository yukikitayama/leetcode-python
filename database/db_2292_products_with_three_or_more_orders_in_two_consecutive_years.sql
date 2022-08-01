-- Find product_id which had 3 or more orders in a year
with cte as (
select
  product_id,
  year(purchase_date) as purchase_year
from
  orders
group by
  product_id,
  year(purchase_date)
having
  count(*) >= 3
)

select
  distinct a.product_id
from
  cte as a
left join
  cte as b
on
  a.product_id = b.product_id
  -- This finds two consecutive years
  and a.purchase_year = b.purchase_year - 1
-- Is not null because null means couldn't find two consecutive years data in self join
where
  b.purchase_year is not null
;
