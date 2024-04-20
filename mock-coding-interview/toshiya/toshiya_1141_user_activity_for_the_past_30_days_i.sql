-- Write your PostgreSQL query statement below
select
  activity_date as day,
  count(distinct user_id) as active_users
from
  activity
where
  -- If period of 2 days and we have 2019-07-27 and 2019-07-26, difference is 1, not 2
  -- That's why 29, not 30.
  '2019-07-27'::date - activity_date between 0 and 29
group by
  1
;