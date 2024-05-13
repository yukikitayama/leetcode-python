-- Write your PostgreSQL query statement below
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
  case
    when b.max_salary < 1000 then a.salary
    when b.max_salary between 1000 and 10000 then round(a.salary * (1 - 0.24))
    else round(a.salary * (1 - 0.49))
  end as salary
from
  salaries as a
left join
  cte as b
on
  a.company_id = b.company_id
;