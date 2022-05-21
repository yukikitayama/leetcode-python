select
  c.customer_name,
  c.customer_id,
  c.order_id,
  c.order_date

from
 (
select
  a.name as customer_name,
  a.customer_id,
  b.order_id,
  b.order_date,
  rank() over(
    partition by
      a.customer_id
    order by
      order_date desc
  ) as 'rank'
from
  customers as a
inner join
  orders as b
on
  a.customer_id = b.customer_id
 ) as c

where
  c.rank <= 3
order by
  1,
  2,
  4 desc
;