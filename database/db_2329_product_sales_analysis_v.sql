# with cte as (
# select
#   a.user_id,
#   a.product_id,
#   a.quantity * b.price as spent
# from
#   sales as a
# left join
#   product as b
# on
#   a.product_id = b.product_id
# )

# select
#   user_id,
#   sum(spent) as spending
# from
#   cte
# group by
#   1
# order by
#   2 desc
# ;

select
  a.user_id,
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
  2 desc
;
