-- Write your PostgreSQL query statement below

-- Find the dep_id which have the largest number of employees
with cte as (
  select
    dep_id,
    rank() over(
       order by count(*) desc
    ) as rank
  from
    employees
  group by
    1
)

select
  b.emp_name as manager_name,
  a.dep_id
from
  cte as a
-- Get the emp_name who belong to those dep_id and position is Manager
join
  employees as b
on
  a.dep_id = b.dep_id
where
  a.rank = 1
  and b.position = 'Manager'
order by
  2
;

