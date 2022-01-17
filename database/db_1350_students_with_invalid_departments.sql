select
  s.id,
  s.name
from
  students as s
left join
  departments as d
on
  s.department_id = d.id
where
  d.name is null