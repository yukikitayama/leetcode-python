# Write your MySQL query statement below
# select
#   name
# from
#   employee
# where
#   id in (
# select
#   managerId
# from
#   employee
# group by
#   managerId
# having
#   count(*) >= 5
#   )
# ;


# select
#   managerId,
#   count(*) as manager_id_count
# from
#   employee
# group by
#   managerId
# having
#   count(*) >= 5


select
  a.name
from
  employee as a
inner join
  (
select
  managerId
from
  employee
group by
  managerId
having
  count(*) >= 5
  ) as b
on
  a.id = b.managerid
;

