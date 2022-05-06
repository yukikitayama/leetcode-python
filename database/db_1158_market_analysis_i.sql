# Write your MySQL query statement below
# select
#   user_id,
#   join_date
# from
#   users

# select
#   buyer_id,
#   count(*) as orders_in_2019
# from
#   orders
# where
#   year(order_date) = 2019
# group by
#   buyer_id
# ;

# select
#   a.user_id as buyer_id,
#   a.join_date,
#   ifnull(b.orders_in_2019, 0) as orders_in_2019
# from
#   users as a
# left join (
#   select
#     buyer_id,
#     count(*) as orders_in_2019
#   from
#     orders
#   where
#     year(order_date) = 2019
#   group by
#     buyer_id
# ) as b
# on
#   a.user_id = b.buyer_id
# ;

select
  a.user_id as buyer_id,
  a.join_date,
  sum(if(year(order_date) = 2019, 1, 0)) as orders_in_2019
from
  users as a
left join
  orders as b
on
  a.user_id = b.buyer_id
group by
  a.user_id
;