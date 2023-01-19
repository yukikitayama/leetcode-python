with

-- Self-join
cte1 as (
  select
    distinct a.user_id,
    b.user_id as recommended_id
  from
    listens as a
  join
    listens as b
  on
    a.song_id = b.song_id
    and a.day = b.day
    and a.user_id != b.user_id
  group by
    a.user_id,
    b.user_id,
    a.day
  having
    count(distinct a.song_id) >= 3
),
-- Modify friendship table to make search easier
cte2 as (
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
  user_id,
  recommended_id
from
  cte1
where
  (user_id, recommended_id) not in (
    select * from cte2
  )
;
