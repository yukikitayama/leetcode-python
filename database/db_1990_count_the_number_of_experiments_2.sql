with
cte1 as (
  select
    'Android' as platform
  union
  select
    'IOS'
  union
  select
    'Web'
),
cte2 as (
  select
    'Reading' as experiment_name
  union
  select
    'Sports'
  union
  select
    'Programming'
),
cte3 as (
  select
    platform,
    experiment_name,
    count(*) as num_experiments
  from
    experiments
  group by
    1,
    2
)

select
  a.platform,
  b.experiment_name,
  ifnull(c.num_experiments, 0) as num_experiments
from
  cte1 as a
cross join
  cte2 as b
left join
  cte3 as c
on
  a.platform = c.platform
  and b.experiment_name = c.experiment_name
;
