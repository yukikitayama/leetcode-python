with cte as (
  select
    *,
    row_number() over(partition by username order by endDate desc) as row_num,
    count(activity) over(partition by username) as activity_count
  from
    useractivity
)

-- select * from cte;

select
  username,
  activity,
  startdate,
  enddate
from
  cte
where
  row_num = 2
  or activity_count = 1
;
