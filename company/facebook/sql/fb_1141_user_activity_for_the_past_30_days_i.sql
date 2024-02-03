-- Write your PostgreSQL query statement below
select
  activity_date as day,
  count(distinct user_id) as active_users
from
  activity
where
  date_part('day', '2019-07-27'::timestamp - activity_date::timestamp) between 0 and 29
group by
  1
;
