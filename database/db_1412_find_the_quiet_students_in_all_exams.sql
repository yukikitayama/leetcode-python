with cte as
(
  select
    exam_id,
    exam.student_id,
    student.student_name,
    score,
    -- Find lowest score by exam_id but use ranking to identify
    rank() over(
      partition by exam_id
      order by score
    ) as rank1,
    -- Find highest score by exam_id but use ranking to identify
    rank() over(
      partition by exam_id
      order by score desc
    ) as rank2
  from exam
  left join student
  on exam.student_id = student.student_id
)

select
  distinct student_id,
  student_name
from
  cte
where
  student_id not in (
    select
      student_id
    from
      cte
    where
      -- Lowest score
      rank1 = 1
      -- Highest score
      or rank2 = 1
  )
order by
  student_id

;
