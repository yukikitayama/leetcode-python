with cte as (
select
  a.project_id,
  max(b.experience_years) as max_year
from
  project as a
left join
  employee as b
on
  a.employee_id = b.employee_id
group by
  1
)

select
  c.project_id,
  d.employee_id
from
  project as c
inner join
  employee as d
on
  c.employee_id = d.employee_id
inner join
  cte as e
on
  c.project_id = e.project_id
  and d.experience_years = e.max_year
;