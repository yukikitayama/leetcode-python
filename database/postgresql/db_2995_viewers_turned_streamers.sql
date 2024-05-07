/*
Find user_id whose first session was viewer
  row_num partition by user_id order by session start
Get user id where row num is 1 and session type is viewer
Count the number of streamers by user id where row num > 1
Join them and show where cuont is not null and count > 0
*/

-- Write your PostgreSQL query statement below
with cte as (
  select
    user_id,
    session_start,
    session_type,
    row_number() over(
      partition by user_id
      order by session_start
    ) as row_num
  from
    sessions
),

cte2 as (
  select
    distinct user_id
  from
    cte
  where
    row_num = 1
    and session_type = 'Viewer'
),

cte3 as (
  select
    user_id,
    count(*) as sessions_count
  from
    cte
  where
    session_type = 'Streamer'
    and row_num > 1
  group by
    1
)

-- select * from cte;
-- select * from cte2;
-- select * from cte3;

select
  a.user_id,
  b.sessions_count
from
  cte2 as a
join
  cte3 as b
on
  a.user_id = b.user_id
order by
  2 desc,
  1 desc
;