with cte as (
  select
    a.platform,
    b.experiment_name
  from
    (
      select
        'Android' as platform
      union
      select
        'IOS'
      union
      select
        'Web'
    ) as a,
    (
      select
        'Reading' as experiment_name
      union
      select
        'Sports'
      union
      select
        'Programming'
    ) as b
)

# select * from cte;

select
  c.platform,
  c.experiment_name,
  ifnull(d.num_experiments, 0) as num_experiments
from
  cte as c
left join (
  select
    platform,
    experiment_name,
    count(*) as num_experiments
  from
    experiments
  group by
    1,
    2
) as d
on
  c.platform = d.platform
  and c.experiment_name = d.experiment_name
;
