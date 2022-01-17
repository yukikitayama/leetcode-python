select
  u.unique_id,
  e.name
from
  employees as e
left join
  employeeuni as u
on
  e.id = u.id