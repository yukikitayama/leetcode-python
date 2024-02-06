-- Write your PostgreSQL query statement below
select
  extra as report_reason,
  count(distinct post_id) as report_count
from
  actions
where
  action = 'report'
  and extra is not null
  and action_date::date = '2019-07-04'
  -- Or simply action_date = '2019-07-04'
group by
  1
;
