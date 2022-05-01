# select
#   id,
#   'Root' as type
# from
#   tree
# where
#   p_id is null

# union

# select
#   id,
#   'Inner' as type
# from
#   tree
# where
#   p_id is not null
#   and id in (
#     select p_id from tree
#   )

# union

# select
#   id,
#   'Leaf' as type
# from
#   tree
# where
#   id not in (
#     select p_id from tree where p_id is not null
#   )
#   # This avoid double counting root
#   and p_id is not null

# order by
#   id

select
  id,
  case
    when p_id is null
      then 'Root'
    when id in (select p_id from tree)
      then 'Inner'
    else 'Leaf'
  end as type
from
  tree
order by
  id