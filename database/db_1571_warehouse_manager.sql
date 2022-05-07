select
  a.name as warehouse_name,
  sum(a.units * b.each_volume) as volume
from
  warehouse as a
left join (
  select
    product_id,
    width * length * height as each_volume
  from
    products
  group by
    product_id
) as b
on
  a.product_id = b.product_id
group by
  a.name
;


--select
--  name as warehouse_name,
--  sum(units * width * length * height) as volume
--from
--  warehouse as a
--left join
--  products as b
--on
--  a.product_id = b.product_id
--group by
--  name
--;