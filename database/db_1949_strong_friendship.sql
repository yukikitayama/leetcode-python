-- self join?

with cte as (
  select
    user1_id,
    user2_id
  from
    friendship

  union

  select
    user2_id as user1_id,
    user1_id as user2_id
  from
    friendship
)

select
  a.user1_id,
  a.user2_id,
  count(c.user2_id) as common_friend
from
  friendship as a
join
  cte as b
on
  a.user1_id = b.user1_id
join
  cte as c
on
  -- This is actually getting user2_id, because in cte, we renamed
  -- user2_id as user1_id
  a.user2_id = c.user1_id
  -- Get user1 and user2 common friend
  and b.user2_id = c.user2_id
group by
  a.user1_id,
  a.user2_id
having
  count(c.user2_id) >= 3
;