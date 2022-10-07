with
-- Find friend IDs of user_id 1
cte1 as (
select
  user2_id as friend_id
from
  friendship
where
  user1_id = 1

-- Use union to find the other direction
union all

select
  user1_id as friend_id
from
  friendship
where
  user2_id = 1
),
-- Find the pages that user_id 1 already liked it
cte2 as (
  select
    distinct page_id
  from
    likes
  where
    user_id = 1
)

select
  distinct page_id as recommended_page
from
  likes
where
  -- page_id which friend likes
  user_id in (
    select * from cte1
  )
  -- and page_id which user_id hasn't like yet
  and page_id not in (
    select * from cte2
  )
;