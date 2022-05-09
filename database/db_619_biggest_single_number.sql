# Write your MySQL query statement below
# select
#   ifnull(
#     (select
#       num
#     from
#       mynumbers
#     group by
#       num
#     having
#       count(*) = 1
#     order by
#       num desc
#     limit
#       1),
#     null
#   ) as num
# ;

select
  max(num) as num
from (
  select
      num
    from
      mynumbers
    group by
      num
    having
      count(*) = 1
    order by
      num desc
    limit
      1
) as a
;