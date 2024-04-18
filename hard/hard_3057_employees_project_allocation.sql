-- Write your PostgreSQL query statement below
with cte as (
  select
    a.*,
    b.name,
    b.team
  from
    project as a
  left join
    employees as b
  on
    a.employee_id = b.employee_id
),

cte2 as (
  select
    team,
    avg(workload) as avg_workload
  from
    cte
  group by
    1
)

select
  a.employee_id,
  a.project_id,
  a.name as employee_name,
  a.workload as project_workload
from
  cte as a
left join
  cte2 as b
on
  a.team = b.team
where
  a.workload > b.avg_workload
order by
  1,
  2
;
