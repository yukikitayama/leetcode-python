# with
# cte1 as (
#   select
#     school_id,
#     score,
#     row_number() over(partition by school_id order by student_count desc, score) as row_num
#   from
#     schools,
#     exam
#   where
#     capacity >= student_count
# ),
# cte2 as (
#   select
#     school_id,
#     score
#   from
#     cte1
#   where
#     row_num = 1
# )

# select
#   a.school_id,
#   ifnull(b.score, -1) score
# from
#   schools as a
# left join
#   cte2 as b
# on
#   a.school_id = b.school_id
# ;

select
  school_id,
  ifnull(min(score), -1) as score
from
  schools
left join
  exam
on
  student_count <= capacity
group by
  1
;
