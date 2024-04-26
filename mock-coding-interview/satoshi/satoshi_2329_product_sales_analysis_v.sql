select
  user_id,
  sum(a.quantity * b.price) as spending
from
  sales as a
left join
  product as b
on
  a.product_id = b.product_id
group by
  1
order by
  2 desc,
  1
;
