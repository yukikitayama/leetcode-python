# Write your MySQL query statement below
# select
#   b.customer_number
# from
#   (
#     select
#       a.customer_number,
#       count(a.order_number)
#     from
#       orders as a
#     group by
#       a.customer_number
#     order by
#       2 desc
#     limit
#       1
#   ) as b
# ;

select
  customer_number
from
  orders
group by
  customer_number
order by
  count(order_number) desc
limit
  1