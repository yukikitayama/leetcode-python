-- Assign team_id by rank of salary
with cte as (
  select
    distinct salary,
    -- Team with lowest salary has team_id = 1
    rank() over(order by salary) as team_id
  from
    employees
  group by
    salary
  having
    -- each team should consist of at least 2 employees
    count(*) > 1
)

select
  a.*,
  b.team_id
from
  employees as a
-- Do not assign unique salary employee to any team,
-- so exclude them by inner join
inner join
  cte as b
on
  a.salary = b.salary
order by
  4,
  1
;
