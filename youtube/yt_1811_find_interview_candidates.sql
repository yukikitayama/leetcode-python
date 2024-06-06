/*
2 190 1 189
2 191 2 189
2 192 3 189
2 194 4 190
2 195 5 190
2 196 6 190
*/

# Write your MySQL query statement below
with cte as (
  select
    gold_medal as gold_user_id
  from
    contests
  group by
    gold_medal
  having
    count(*) >= 3
),

cte2 as (
  select
    gold_medal as user_id,
    contest_id
  from
    contests
  union all
  select
    silver_medal as user_id,
    contest_id
  from
    contests
  union all
  select
    bronze_medal as user_id,
    contest_id
  from
    contests
),

cte3 as (
  select
    user_id,
    contest_id - row_number() over(partition by user_id order by contest_id) as group_id
  from
    cte2
),

cte4 as (
  select
    distinct user_id
  from
    cte3
  group by
    user_id,
    group_id
  having
    count(*) >= 3
)

-- select * from cte;
-- select * from cte2;
-- select * from cte3 order by user_id, group_id;
-- select * from cte4;

select
  name,
  mail
from
  users
where
  user_id in (
    select gold_user_id from cte
  )
  or user_id in (
    select user_id from cte4
  )
;
