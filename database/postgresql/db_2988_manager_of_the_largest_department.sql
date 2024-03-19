-- Write your PostgreSQL query statement below
with cte as (
  select
    dep_id,
    rank() over(order by count(*) desc) as rnk
  from
    employees
  group by
    1
)

select
  emp_name as manager_name,
  dep_id
from
  employees
where
  dep_id in (
    select dep_id from cte where rnk = 1
  )
  and position = 'Manager'
order by
  2
;
