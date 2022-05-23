select
  a.employee_id
from
  employees as a,
  employees as b,
  employees as c
where
  a.manager_id = b.employee_id
  and b.manager_id = c.employee_id
  and c.manager_id = 1
  and a.employee_id != 1