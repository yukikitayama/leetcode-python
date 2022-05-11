select
  a.student_id,
  a.student_name,
  b.subject_name,
  count(c.subject_name) as attended_exams
from
  students as a
inner join
  subjects as b
left join
  examinations as c
on
  a.student_id = c.student_id
  and b.subject_name = c.subject_name
group by
  a.student_id,
  b.subject_name
order by
  1,
  3
;