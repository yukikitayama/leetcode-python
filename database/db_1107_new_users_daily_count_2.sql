with
cte as (
select
  user_id,
  min(activity_date) as first_login_date
from
  traffic
where
  activity = 'login'
group by
  1
)

-- select * from cte;

select
  first_login_date as login_date,
  count(distinct user_id) as user_count
from
  cte
where
  datediff('2019-06-30', first_login_date) <= 90
group by
  1
;