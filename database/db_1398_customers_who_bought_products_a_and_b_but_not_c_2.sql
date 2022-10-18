# with
# cte1 as (
#   select
#     distinct customer_id as a_buyer
#   from
#     orders
#   where
#     product_name = 'A'
# ),
# cte2 as (
#   select
#     distinct customer_id as b_buyer
#   from
#     orders
#   where
#     product_name = 'B'
# ),
# cte3 as (
#   select
#     distinct customer_id as c_buyer
#   from
#     orders
#   where
#     product_name = 'C'
# )

# select
#   customer_id,
#   customer_name
# from
#   customers
# where
#   customer_id in (select * from cte1)
#   and customer_id in (select * from cte2)
#   and customer_id not in (select * from cte3)
# order by
#   1
# ;

select
  a.customer_id,
  a.customer_name
from
  customers as a,
  orders as b
where
  a.customer_id = b.customer_id
group by
  a.customer_id
having
  sum(b.product_name = 'A') > 0
  and sum(b.product_name = 'B') > 0
  and sum(b.product_name = 'C') = 0
order by
  1
;
