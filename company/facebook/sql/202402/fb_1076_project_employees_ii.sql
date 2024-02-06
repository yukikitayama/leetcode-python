-- Write your PostgreSQL query statement below
with cte as (
  select
    project_id,
    count(distinct employee_id) as num_employee
  from
    project
  group by
    1
)

select
  project_id
from
  cte
where
  num_employee = (
    select max(num_employee) from cte
  )
;