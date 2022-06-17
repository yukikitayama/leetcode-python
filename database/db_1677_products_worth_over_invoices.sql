select
  a.name,
  ifnull(sum(b.rest), 0) as rest,
  ifnull(sum(b.paid), 0) as paid,
  ifnull(sum(b.canceled), 0) as canceled,
  ifnull(sum(b.refunded), 0) as refunded
from
  product as a
left join
  invoice as b
on
  a.product_id = b.product_id
group by
  1
order by
  1
;
