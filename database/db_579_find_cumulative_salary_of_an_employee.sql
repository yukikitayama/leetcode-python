select
  b.id,
  b.month,
  -- By left join, salary could be null. To make sum possible
  -- if null, overwrite it to 0
  ifnull(b.salary, 0) + ifnull(c.salary, 0) + ifnull(d.salary, 0) as salary
from
  (
  select
    id,
    max(month) as month
  from
    employee
  group by
    id
  having
    count(*) > 1
  ) as a
  left join
    employee as b
  on
    a.id = b.id
    -- Exclude the recent month by id
    and a.month > b.month
  -- Previous month salary
  left join
    employee as c
  on
    c.id = b.id
    and c.month = b.month - 1
  -- Previous previous month
  left join
    employee as d
  on
    d.id = b.id
    and d.month = b.month - 2
order by
  1,
  2 desc

;
