with
cte1 as (
select
  employee_id,
  sum(ceiling(timestampdiff(second, in_time, out_time) / 60)) as minute_work
from
  logs
group by
  1
)

select
  a.employee_id
from
  employees as a
left join
  cte1 as b
on
  a.employee_id = b.employee_id
where
  a.needed_hours * 60 > ifnull(b.minute_work, 0)
;