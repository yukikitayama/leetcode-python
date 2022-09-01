with cte as (
  select
    name,
    salary,
    departmentid,
    rank() over(partition by departmentid order by salary desc) as rnk
  from
    employee
)

select
  b.name as department,
  a.name as employee,
  a.salary
from
  cte as a
left join
  department as b
on
  a.departmentid = b.id
where
  a.rnk = 1
;