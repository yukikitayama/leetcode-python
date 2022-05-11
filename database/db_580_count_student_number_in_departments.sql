select
  dept_name,
  count(student_id) as student_number
from
  department as a
left join
  student as b
on
  a.dept_id = b.dept_id
group by
  dept_name
order by
  student_number desc,
  dept_name
;
