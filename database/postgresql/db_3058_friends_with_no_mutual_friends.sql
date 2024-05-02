-- Write your PostgreSQL query statement below
with cte as (
  select
    user_id1 as this_id,
    user_id2 as other_id
  from
    friends
  union all
  select
    user_id2 as this_id,
    user_id1 as other_id
  from
    friends
),

cte2 as (
  select
    -- Pair of ID who share a friend
    a.this_id as user_id1,
    b.this_id as user_id2
  from
    cte as a
  inner join
    cte as b
  on
    a.other_id = b.other_id
)

-- select * from cte;
-- select * from cte2;

select
  user_id1,
  user_id2
from
  friends
where
  (user_id1, user_id2) not in (
    select user_id1, user_id2 from cte2
  )
order by
  1,
  2
;

