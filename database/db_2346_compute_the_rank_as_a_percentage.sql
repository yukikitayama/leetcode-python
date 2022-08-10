with
-- Rank of each student in their department
cte1 as (
select
  student_id,
  department_id,
  rank() over(partition by department_id order by mark desc) as rnk
from
  students
),
-- Number of students in each department
cte2 as (
select
  department_id,
  count(*) as cnt
from
  students
group by
  1
)

-- select * from cte1;
-- select * from cte2;

select
  a.student_id,
  a.department_id,
  -- When number of students in a department is 1, the below returns null, but the problem wants it to be 0
  ifnull(round(((a.rnk - 1) / (b.cnt - 1)) * 100, 2), 0) as percentage
from
  cte1 as a
left join
  cte2 as b
on
  a.department_id = b.department_id
;
