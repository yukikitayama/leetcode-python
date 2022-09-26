with cte as (
  select
    student_id,
    course_id,
    grade,
    -- Compute rank to find the highest grade for each student and by course ID
    rank() over(
      -- Highest grade by student
      partition by student_id
      -- In case of a tie, find the course with the smallest course_id
      order by grade desc, course_id
    ) as rnk
  from
    enrollments
)

select
  student_id,
  course_id,
  grade
from
  cte
where
  -- The row with the highest grade has rank 1
  rnk = 1
order by
  1
;