# Write your MySQL query statement below
# select
#   distinct a.school_id,
#   ifnull(score, -1) as score
# from
#   schools as a
# left join
#   (
# select
#   school_id,
#   min(score) as score
# from
#   schools,
#   exam
# where
#   student_count <= capacity
# group by
#   school_id
#   ) as b
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
  school_id
;