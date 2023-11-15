with

marketing as (
  select
    max(salary) as max_salary
  from
    salaries
  where
    department = 'Marketing'
),

engineering as (
  select
    max(salary) as max_salary
  from
    salaries
  where
    department = 'Engineering'
)

select
  abs(a.max_salary - b.max_salary) as salary_difference
from
  marketing as a,
  engineering as b
;

