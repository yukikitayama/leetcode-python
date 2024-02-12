
/*
friendship union itself to get friends id of each user

To above table, outer join likes table
  by above friends id equal to likes user_id

By user_id and page_id
  group by count friends id

*/

with cte as (
  select
    user1_id as user_id,
    user2_id as friend_id
  from
    friendship
  union
  select
    user2_id as user_id,
    user1_id as friend_id
  from
    friendship
),

cte2 as (
  select
    a.user_id,
    b.page_id,
    count(distinct a.friend_id) as friends_likes
  from
    cte as a
  full outer join
    likes as b
  on
    a.friend_id = b.user_id
  group by
    1,
    2
  order by
    a.user_id
)

select
  user_id,
  page_id,
  friends_likes
from
  cte2
where
  (user_id, page_id) not in (
    select user_id, page_id from likes
  )
;
