with cte as (
  select
    product_id,
    year(purchase_date) as purchase_year,
    row_number() over(
      partition by product_id
      order by year(purchase_date)
    ) as row_num
  from
    orders
  group by
    1,
    2
  having
    count(order_id) >= 3
)

select
  distinct product_id
from
  cte
group by
  product_id,
  purchase_year - row_num
having
  count(*) >= 2
;
