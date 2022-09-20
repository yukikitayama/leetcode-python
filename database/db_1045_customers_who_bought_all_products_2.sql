select
  customer_id
from
  customer
group by
  1
having
  count(distinct product_key) = (
    select count(distinct product_key) from product
  )
;