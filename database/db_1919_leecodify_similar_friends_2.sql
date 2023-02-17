with
cte1 as (
  select
    a.user_id as user1_id,
    b.user_id as user2_id,
    a.song_id,
    a.day
  from
    listens as a,
    listens as b
  where
    -- Find same songs on the same day
    a.song_id = b.song_id
    and a.day = b.day
    -- Filter they are friend
    and (a.user_id, b.user_id) in (
      select * from friendship
    )
),
cte2 as (
  select
    -- Distinct because group by having gives us the multiple rows with the
    -- condition, but we only unique ID combinaiton which satisfy the condition
    distinct user1_id,
    user2_id
  from
    cte1
  group by
    user1_id,
    user2_id,
    day
  having
    -- Count 3 or more different songs
    count(distinct song_id) >= 3
)

select * from cte2;