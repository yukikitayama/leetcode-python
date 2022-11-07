with
-- The user who won the gold medal in 3 or more different contests
cte1 as (
  select
    gold_medal as user_id
  from
    contests
  group by
    1
  having count(*) >= 3
),
-- Create a table which vertically contain all the information
cte2 as (
  select
    contest_id,
    gold_medal as user_id
  from
    contests
  union all
  select
    contest_id,
    silver_medal as user_id
  from
    contests
  union all
  select
    contest_id,
    bronze_medal as user_id
  from
    contests
),
-- Compute row number to later take difference from contest_id to make a group ID
-- for consecutive contests
cte3 as (
  select
    *,
    row_number() over(partition by user_id order by contest_id) as row_num
  from
    cte2
),
-- Find user_id who won any medal in 3 or more consecutive contests
cte4 as (
  select
    distinct user_id
  from
    cte3
  group by
    user_id,
    -- This difference will be constant if both contest_id and row number are consecutive
    -- so that we can create a group ID
    contest_id - row_num
  having
    count(*) >= 3
)

select
  name,
  mail
from
  users
where
  -- The user won the gold medal in three or more different contests (not necessarily consecutive)
  user_id in (select * from cte1)
  -- The user won any medal in three or more consecutive contests
  or user_id in (select * from cte4)
;
