-- Write your PostgreSQL query statement below
select
  a.student_id,
  a.student_name,
  b.subject_name,
  sum(case when c.subject_name is not null then 1 else 0 end) as attended_exams
from
  students as a
cross join
  subjects as b
left join
  examinations as c
on
  a.student_id = c.student_id
  and b.subject_name = c.subject_name
group by
  1,
  2,
  3
order by
  1,
  3
;
