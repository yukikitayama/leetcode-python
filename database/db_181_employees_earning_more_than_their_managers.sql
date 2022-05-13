# Write your MySQL query statement below
select
  # a.id,
  # a.name,
  # a.salary,
  # a.managerid,
  # b.salary
  a.name as employee
from
  employee as a
left join
  employee as b
on
  a.managerid = b.id
where
  a.salary > b.salary
;
