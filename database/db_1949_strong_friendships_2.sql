-- Make bidirectonal table to be able to count easily
with cte as (
  select
    user1_id as me,
    user2_id as you
  from
    friendship
  union all
  select
    user2_id as me,
    user1_id as you
  from
    friendship
)

select
  a.me as user1_id,
  b.me as user2_id,
  count(*) as common_friend
from
  -- Self-join
  cte as a,
  cte as b
where
  -- They have the common friend
  a.you = b.you
  -- We only care when user1_id < user2_id
  and a.me < b.me
  -- They are actually friend
  and (a.me, b.me) in (select * from friendship)
group by
  1,
  2
having
  -- They have at least 3 common friends
  count(*) >= 3
;