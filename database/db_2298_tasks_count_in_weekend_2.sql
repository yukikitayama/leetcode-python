# with cte as (
# select
#   case
#     when weekday(submit_date) in (5, 6) then 'weekend'
#     else 'working'
#   end as weekday_type,
#   count(task_id) as cnt
# from
#   tasks
# group by
#   1
# )

# select
#   sum(if(weekday_type = 'weekend', cnt, 0)) as weekend_cnt,
#   sum(if(weekday_type = 'working', cnt, 0)) as working_cnt
# from
#   cte
# ;

select
  sum(case
    when weekday(submit_date) in (5, 6) then 1
    else 0
  end) as weekend_cnt,
  sum(case
    when weekday(submit_date) in (0, 1, 2, 3, 4) then 1
    else 0
  end) as working_cnt
from
  tasks
;