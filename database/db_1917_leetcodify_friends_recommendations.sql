-- Get number of same songs by two users
# select
#   a.user_id as this_user_id,
#   b.user_id as that_user_id
# from
#   listens as a,
#   listens as b
# where
#   a.day = b.day
#   and a.song_id = b.song_id
#   and a.user_id <> b.user_id
# group by
#   1,
#   2
# having
#   count(*) >= 3

# select
#   user1_id,
#   user2_id
# from
#   friendship
# union all
# select
#   user2_id as user1_id,
#   user1_id as user2_id
# from
#   friendship

# select
#   a.user_id as user_id,
#   b.user_id as recommended_id
# from
#   listens as a,
#   listens as b
# where
#   a.day = b.day
#   and a.song_id = b.song_id
#   and a.user_id <> b.user_id
#   and (a.user_id, b.user_id) not in (
#   select
#   user1_id,
#   user2_id
# from
#   friendship
# union all
# select
#   user2_id as user1_id,
#   user1_id as user2_id
# from
#   friendship
#   )
# group by
#   1,
#   2,
#   a.day
# having
#   count(distinct a.song_id) >= 3

with cte1 as (
  select
    a.user_id as user1_id,
    b.user_id as user2_id,
    count(distinct a.song_id) as count_songs
  from
    listens as a
  join
    listens as b
  on
    a.song_id = b.song_id
    and a.day = b.day
    and a.user_id <> b.user_id
  -- x and y listened to the same song on the same day
  group by
    a.user_id,
    b.user_id,
    a.day
  -- Three or more different songs
  having
    count_songs >= 3
),

-- Make bidirectional table
cte2 as (
  select
    user1_id,
    user2_id
  from
    friendship
  union all
  select
    user2_id as user1_id,
    user1_id as user2_id
  from
    friendship
)

select
  -- distinct because duplicates are not allowed, ie. y should not be recommended
  -- to x multiple times
  distinct user1_id as user_id,
  user2_id as recommended_id
from
  cte1
where
  (user1_id, user2_id) not in (
    select
      user1_id,
      user2_id
    from
      cte2
  )

# with c as (
#     select l1.user_id as uid1, l2.user_id as uid2, count(distinct l1.song_id) as ct
#     from listens l1
#     join listens l2
#     on l1.song_id=l2.song_id and l1.day=l2.day and l1.user_id<>l2.user_id  # make sure l1.user_id != l2.user_id, we don't wanna join on user_id itself
#     group by l1.user_id, l2.user_id, l1.day
#     having ct>=3  # make sure the number of different songs on each day >=3
# ), f (uid1, uid2) as (
#     select user1_id, user2_id from friendship
#     union
#     select user2_id, user1_id from friendship
# )
# select uid1 as user_id, uid2 as recommended_id
# from c
# where (uid1, uid2) not in (select uid1, uid2 from f)
# group by uid1, uid2

;


