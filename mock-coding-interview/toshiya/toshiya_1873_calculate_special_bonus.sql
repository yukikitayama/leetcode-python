-- Write your PostgreSQL query statement below
select
  employee_id,
  case
    when employee_id % 2 != 0 and left(name, 1) != 'M' then salary
    else 0
  end as bonus
from
  employees
order by
  1
;
