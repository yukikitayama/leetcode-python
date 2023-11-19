select
  a.user_id,
  a.steps_date,
  round((a.steps_count + b.steps_count + c.steps_count) / 3, 2) as rolling_average
from
  steps as a
left join
  steps as b
on
  a.steps_date = date_add(b.steps_date, interval 1 day)
  and a.user_id = b.user_id
left join
  steps as c
on
  a.steps_date = date_add(c.steps_date, interval 2 day)
  and a.user_id = c.user_id
where
  b.user_id is not null
  and c.user_id is not null
order by
  1,
  2
;
