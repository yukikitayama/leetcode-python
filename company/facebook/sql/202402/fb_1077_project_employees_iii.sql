-- Write your PostgreSQL query statement below
with cte as (
  select
    a.project_id,
    b.employee_id,
    dense_rank() over(
      partition by a.project_id
      order by b.experience_years desc
    ) as rnk
  from
    project as a
  left join
    employee as b
  on
    a.employee_id = b.employee_id
)

select
  project_id,
  employee_id
from
  cte
where
  rnk = 1
;
