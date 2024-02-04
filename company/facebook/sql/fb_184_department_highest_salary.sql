-- Write your PostgreSQL query statement below
with
highest_salary as (
  select
    departmentid,
    max(salary) as salary
  from
    employee
  group by
    1
)

select
  c.name as Department,
  a.name as Employee,
  a.salary as Salary
from
  employee as a
inner join
  highest_salary as b
on
  a.salary = b.salary
  and a.departmentid = b.departmentid
left join
  department as c
on
  a.departmentid = c.id
;