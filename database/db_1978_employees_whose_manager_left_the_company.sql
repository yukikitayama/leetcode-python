select
  a.employee_id
from
  employees as a
left join
  employees as b
on
  a.manager_id = b.employee_id
where
  a.salary < 30000
  and a.manager_id is not null
  and b.employee_id is null
order by
  1
;