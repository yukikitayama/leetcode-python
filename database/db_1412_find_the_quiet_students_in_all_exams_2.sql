with
-- Find low and high score for each exam
cte1 as (
  select
    exam_id,
    min(score) as low,
    max(score) as high
  from
    exam
  group by
    1
),
-- Find student ID who got low or high score
cte2 as (
  select
    distinct a.student_id
  from
    exam as a
  left join
    cte1 as b
  on
    a.exam_id = b.exam_id
    and (
      a.score = b.low
      or a.score = b.high
    )
  where
    low is not null
    or high is not null
)

-- select * from cte1;
-- select * from cte2;
select
  distinct a.student_id,
  b.student_name
from
  exam as a
left join
  student as b
on
  a.student_id = b.student_id
where
  a.student_id not in (
    select * from cte2
  )
order by
  1
;