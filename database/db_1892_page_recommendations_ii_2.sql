with

-- Transform friendship table
cte1 as (
  select
    user1_id,
    user2_id
  from
    friendship
  -- Use union to remove duplicates, not union all
  union
  select
    user2_id as user1_id,
    user1_id as user2_id
  from
    friendship
)

select
  a.user1_id as user_id,
  b.page_id,
  count(distinct a.user2_id) as friends_likes
from
  cte1 as a
left join
  likes as b
on
  a.user2_id = b.user_id

# where
#   (a.user1_id, b.page_id) not in (
#     select
#       user_id,
#       page_id
#     from
#       likes
# )

-- Find pages liked by themselve, and if they are joined,
-- we need to exclude, so where statement is null
left join
  likes as c
on
  a.user1_id = c.user_id
  and b.page_id = c.page_id
where
  c.page_id is null

group by
  1,
  2
;