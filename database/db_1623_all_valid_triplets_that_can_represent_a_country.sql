select
  a.student_name as member_a,
  b.student_name as member_b,
  c.student_name as member_c
from
  schoola as a,
  schoolb as b,
  schoolc as c
where
  a.student_name != b.student_name
  and b.student_name != c.student_name
  and c.student_name != a.student_name
  and a.student_id != b.student_id
  and b.student_id != c.student_id
  and c.student_id != a.student_id
;
