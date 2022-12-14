with cte as (
select
  departmentId,
  salary,
  dense_rank() over(
    partition by departmentId
    order by salary desc
  ) as rnk
from
  employee
)

-- select * from cte order by 1, 2 desc;
-- select * from cte where rnk <= 3;

select
  b.name as department,
  a.name as employee,
  a.salary
from
  employee as a
left join
  department as b
on
  a.departmentId = b.id
where
  (a.departmentId, a.salary) in (
    select departmentId, salary from cte where rnk <= 3
  )
;
