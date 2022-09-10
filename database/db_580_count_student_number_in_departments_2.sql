# with cte as (
# select
#   dept_id,
#   count(distinct student_id) as student_number
# from
#   student
# group by
#   1
# )

# -- select * from cte;

# select
#   a.dept_name,
#   ifnull(b.student_number, 0) as student_number
# from
#   department as a
# left join
#   cte as b
# on
#   a.dept_id = b.dept_id
# order by
#   2 desc,
#   1
# ;

select
  a.dept_name,
  count(b.student_id) as student_number
from
  department as a
left join
  student as b
on
  a.dept_id = b.dept_id
group by
  1
order by
  2 desc,
  1
;
