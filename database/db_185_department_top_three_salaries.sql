with cte as (
select
  departmentid,
  name,
  salary,
  dense_rank() over(
    partition by departmentid
    order by salary desc
  ) as 'rank'
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
  a.rank <= 3
;
