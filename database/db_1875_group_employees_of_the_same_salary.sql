select
  employee_id,
  name,
  salary,
  dense_rank() over(order by salary) as team_id
from
  employees
where
  salary in (
-- Find salaries which have at least two employees with
select
  salary
from
  employees
group by
  salary
having
  count(*) > 1
  )
order by
  4,
  1
;