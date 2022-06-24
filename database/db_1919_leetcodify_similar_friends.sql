select
  distinct a.user_id as user1_id,
  b.user_id as user2_id
from
  listens as a,
  listens as b
where
  a.day = b.day
  and a.song_id = b.song_id
  and a.user_id <> b.user_id
  and (a.user_id, b.user_id) in (
    select
      user1_id,
      user2_id
    from
      friendship
  )
group by
  1,
  2,
  a.day
having
  count(distinct a.song_id) >= 3
;

