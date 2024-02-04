with cte as (
  select
    b.name as department,
    a.name as employee,
    a.salary as salary,
    dense_rank() over(
      partition by a.departmentid
      order by a.salary desc
    ) as rnk
  from
    employee as a
  left join
    department as b
  on
    a.departmentid = b.id
)

select
  department,
  employee,
  salary
from
  cte
where
  rnk <= 3
;