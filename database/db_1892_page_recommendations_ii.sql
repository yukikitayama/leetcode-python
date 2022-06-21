with cte1 as (
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

# select * from cte1 where user1_id = 1;

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
-- Filter out pages that are already like by the user
left join
  likes as c
on
  a.user1_id = c.user_id
  and b.page_id = c.page_id
-- b.page_id is page that friends like
-- c.page_id is page that users like
-- So as long as c.page_id is null, the b.page_id is friends like, but user didn't like
where
  c.page_id is null

group by
  1,
  2

