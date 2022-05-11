# Write your MySQL query statement below
select
  b.name as department,
  a.name as employee,
  a.salary
from
  employee as a
inner join
  department as b
on
  a.departmentid = b.id
where
  (a.departmentid, a.salary) in (
select
  departmentid,
  max(salary) as highest_salary
from
  employee
group by
  departmentid
  )
;
