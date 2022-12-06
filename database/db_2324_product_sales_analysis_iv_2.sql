# with
# cte1 as (
#     select
#       a.user_id,
#       a.product_id,
#       sum(a.quantity * b.price) as total_spent
#     from
#       sales as a
#     left join
#       product as b
#     on
#       a.product_id = b.product_id
#     group by
#       1,
#       2
# ),
# cte2 as (
#     select
#         user_id,
#         max(total_spent) as max_spent
#     from
#         cte1
#     group by
#         1
# )

# select
#     cte1.user_id,
#     cte1.product_id
# from
#     cte1
# join
#     cte2
# on
#     cte1.user_id = cte2.user_id
#     and cte1.total_spent = cte2.max_spent

with cte as (
    select
        a.user_id,
        a.product_id,
        rank() over(
            partition by a.user_id
            order by sum(a.quantity * b.price) desc
        ) as rnk
    from
        sales as a
    left join
        product as b
    on
        a.product_id = b.product_id
    group by
        1,
        2
)

select
  user_id,
  product_id
from
  cte
where
  rnk = 1
;