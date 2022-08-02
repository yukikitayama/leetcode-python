with cte as (
  select
    case
      when weekday(submit_date) in (5, 6) then 1
      else 0
    end as weekend,
    count(*) as cnt
  from
    tasks
  group by
    1
)

# select * from cte;

select
  *
from
  (
select
  cnt as weekend_cnt
from
  cte
where
  weekend = 1
  ) as a,
  (
select
  cnt as working_cnt
from
  cte
where
  weekend = 0
  ) as b

# select
#   sum(weekday(submit_date) >= 5) as weekend_cnt,
#   sum(weekday(submit_date) < 5) as working_cnt
# from
#   tasks
# ;