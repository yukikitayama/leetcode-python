-- Write your PostgreSQL query statement below

/*
Query
  group by user_id
  count distinct session_id
  where last 30 days

  Put above to CTE

  Average the count
*/

with cte as (
  select
    user_id,
    count(distinct session_id) as session_count
  from
    activity
  where
    date_part('day', '2019-07-27'::timestamp - activity_date) < 30
  group by
    user_id
)

select
  -- MySQL IFNULL doesn't exist in PostgreSQL
  coalesce(round(avg(session_count), 2), 0) as average_sessions_per_user
from
  cte
;


