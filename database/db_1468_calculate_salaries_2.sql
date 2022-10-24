-- Find max salary for each company
with cte as (
  select
    company_id,
    max(salary) as max_salary
  from
    salaries
  group by
    1
)

select
  a.company_id,
  a.employee_id,
  a.employee_name,
  -- Compute tax of each employee and subtract it from salary of each employee
  round(a.salary - a.salary * case
    when b.max_salary < 1000 then 0
    when b.max_salary > 10000 then 0.49
    else 0.24
  end, 0) as salary
from
  salaries as a
-- Join max salary of each company to get tax rate of each employee
left join
  cte as b
on
  a.company_id = b.company_id
;
