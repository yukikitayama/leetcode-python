select
  min_activity_date as login_date,
  count(user_id) as user_count
from (
select
  user_id,
  min(activity_date) as min_activity_date
from
  traffic
where
  activity = 'login'
group by
  user_id
) as a
where
  datediff('2019-06-30', min_activity_date) <= 90
group by
  1
order by
  1
;
