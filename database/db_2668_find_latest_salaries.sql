
with cte as (
  select
    *,
    row_number() over(partition by emp_id order by salary desc) as row_num
  from
    salary
)

select
  emp_id,
  firstname,
  lastname,
  salary,
  department_id
from
  cte
where
  row_num = 1
order by
  emp_id
;