-- Compute total minutes each employee worked
with cte as (
  select
    employee_id,
    -- ceiling() to round up minutes by seconds worked
    sum(ceiling(timestampdiff(second, in_time, out_time) / 60)) as total_minute
  from
    logs
  group by
    1
)

select
  a.employee_id
from
  employees as a
left join
  cte as b
on
  a.employee_id = b.employee_id
where
  -- ifnull because if an employee didn't work, left join gives us null
  -- But we need to report this type of employee too.
  a.needed_hours * 60 > ifnull(b.total_minute, 0)
;
