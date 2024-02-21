-- Write your PostgreSQL query statement below
select
  *,
  case
    when x + y <= z then 'No'
    when y + z <= x then 'No'
    when z + x <= y then 'No'
    else 'Yes'
  end as triangle
from
  triangle
;
