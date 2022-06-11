-- Verions 1
# select
#   customer_id,
#   name
# from
#   customers
# where
#   customer_id in (
# select
#   c.customer_id
# from (
# select
#   a.customer_id,
#   year(order_date) as year_order,
#   month(order_date) as month_order,
#   sum(a.quantity * b.price) as total_spent
# from
#   orders as a
# left join
#   product as b
# on
#   a.product_id = b.product_id
# group by
#   1,
#   2,
#   3
# having
#   total_spent >= 100
#   and year_order = 2020
#   and month_order in (6, 7)
# ) as c
# group by
#   1
# having
#   count(*) > 1
# )
# ;

-- Verions 2
select
  a.customer_id,
  a.name
from
  customers as a
join
  orders as b
on
  a.customer_id = b.customer_id
join
  product as c
on
  b.product_id = c.product_id
group by
  a.customer_id
having
  sum(
    if(
      left(b.order_date, 7) = '2020-06',
      b.quantity,
      0
    ) * c.price
  ) >= 100
  and sum(
    if(
      left(b.order_date, 7) = '2020-07',
      b.quantity,
      0
    ) * c.price
  ) >= 100
;
