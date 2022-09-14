-- Root if p_id is null
-- Inner if it has p_id and other node use this node as p_id
-- Leaf if it has p_id and other node don't use this node as p_id

# with
# -- Root
# cte1 as (
# select
#   id
# from
#   tree
# where
#   p_id is null
# ),

# -- Leaf
# cte2 as (
# select
#   distinct id
# from
#   tree
# where
#   id not in (
#     select
#       distinct p_id
#     from
#       tree
#     where
#       p_id is not null
#   )
# ),

# -- Inner
# cte3 as (
# select
#   distinct id
# from
#   tree
# where
#   id in (
#     select
#       distinct p_id
#     from
#       tree
#     where
#       p_id is not null
#   )
#   and p_id is not null
# )

# select
#   a.id,
#   case
#     when b.id is not null then 'Root'
#     when c.id is not null then 'Leaf'
#     when d.id is not null then 'Inner'
#   end as type
# from
#   tree as a
# left join
#   cte1 as b
# on
#   a.id = b.id
# left join
#   cte2 as c
# on
#   a.id = c.id
# left join
#   cte3 as d
# on
#   a.id = d.id
# order by
#   a.id
# ;

select
  id,
  case
    when id = (select id from tree where p_id is null) then 'Root'
    when id in (select p_id from tree) then 'Inner'
    else 'Leaf'
  end as type
from
  tree
order by
  1
;