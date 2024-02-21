-- Write your PostgreSQL query statement below

with cte as (
  select
    departmentId,
    max(salary) as max_salary
  from
    employee
  group by
    1
)

select
  b.name as Department,
  a.name as Employee,
  a.salary
from
  employee as a
left join
  department as b
on
  a.departmentId = b.id
where
  (a.departmentId, a.salary) in (
    select departmentId, max_salary from cte
  )
;
