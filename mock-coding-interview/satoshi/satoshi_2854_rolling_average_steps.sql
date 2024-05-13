-- Write your PostgreSQL query statement below

select
  a.user_id,
  a.steps_date,
  round((a.steps_count + b.steps_count + c.steps_count)::decimal / 3, 2) as rolling_average
from
  steps as a
left join
  steps as b
on
  b.user_id = a.user_id
  and b.steps_date = a.steps_date - 1
left join
  steps as c
on
  c.user_id = a.user_id
  and c.steps_date = a.steps_date - 2
where
  b.steps_count is not null
  and c.steps_count is not null
order by
  1,
  2
;