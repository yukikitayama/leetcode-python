-- Write your PostgreSQL query statement below

/*
union friendship with itself
  the other table swap columns

join likes to above table by above.user2_id = likes.user_id
  outer join
  where above.user1_id = 1

get page_id from the joined table
  where page_id not in the page_id list that user_id 1 likes
*/

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
),

cte2 as (
  select
    *
  from
    cte as a
  -- Error if you omit full
  full outer join
    likes as b
  on
    a.user2_id = b.user_id
  where
    a.user1_id = 1
)

-- select * from cte2;

select
  distinct page_id as recommended_page
from
  cte2
where
  -- Without this, one null row will be returned,
  -- and it won't pass the test case where likes table doesn't contain friends of user_id 1
  page_id is not null
  and page_id not in (
    select page_id from likes where user_id = 1
  )
;



