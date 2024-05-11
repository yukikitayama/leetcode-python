-- Write your PostgreSQL query statement below
select
  contest_id,
  round(count(distinct user_id)::decimal / (select count(distinct user_id) from users) * 100, 2) as percentage
from
  register
group by
  1
order by
  2 desc,
  1
;