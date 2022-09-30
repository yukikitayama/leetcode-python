with cte as (
select
  buyer_id,
  count(distinct order_id) as orders_in_2019
from
  orders
where
  year(order_date) = 2019
group by
  1
)

select
  a.user_id as buyer_id,
  a.join_date,
  ifnull(b.orders_in_2019, 0) as orders_in_2019
from
  users as a
left join
  cte as b
on
  a.user_id = b.buyer_id
;
