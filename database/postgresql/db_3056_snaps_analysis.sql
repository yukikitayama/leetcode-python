-- Write your PostgreSQL query statement below

with cte as (
  select
    b.age_bucket,
    a.activity_type,
    sum(a.time_spent) as sum_time
  from
    activities as a
  left join
    age as b
  on
    a.user_id = b.user_id
  group by
    1,
    2
)

select
  a.age_bucket,
  round(coalesce(a.sum_time, 0)::decimal / (coalesce(a.sum_time, 0) + coalesce(b.sum_time, 0)) * 100, 2) as send_perc,
  round(coalesce(b.sum_time, 0)::decimal / (coalesce(a.sum_time, 0) + coalesce(b.sum_time, 0)) * 100, 2) as open_perc
from
  (select age_bucket, sum_time from cte where activity_type = 'send') as a
full outer join
  (select age_bucket, sum_time from cte where activity_type = 'open') as b
on
  a.age_bucket = b.age_bucket
;

-- select
--   b.age_bucket,
--   round(sum(case when a.activity_type = 'send' then a.time_spent else 0 end)::decimal / sum(a.time_spent) * 100, 2) as send_perc,
--   round(sum(case when a.activity_type = 'open' then a.time_spent else 0 end)::decimal / sum(a.time_spent) * 100, 2) as open_perc
-- from
--   activities as a
-- left join
--   age as b
-- on
--   a.user_id = b.user_id
-- group by
--   1
-- ;