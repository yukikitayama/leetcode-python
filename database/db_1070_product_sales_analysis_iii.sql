with
cte as (
  select
    product_id,
    min(year) as first_year
  from
    sales
  group by
    1
)

select
  a.product_id,
  a.year as first_year,
  a.quantity,
  a.price
from
  sales as a
inner join
  cte as b
on
  a.product_id = b.product_id
  and a.year = b.first_year
;
