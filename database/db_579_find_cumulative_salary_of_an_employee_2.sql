with
-- Most recent month by employee
cte1 as (
  select
    id,
    max(month) as recent_month
  from
    employee
  group by
    1
),
cte2 as (
  select
    a.id,
    a.month,
    (
      ifnull(a.salary, 0)
      + ifnull(b.salary, 0)
      + ifnull(c.salary, 0)
     ) as salary
  from
    employee as a
  left join
    employee as b
  on
    a.id = b.id
    and a.month = b.month + 1
  left join
    employee as c
  on
    a.id = c.id
    and a.month = c.month + 2
)

-- select * from cte1;
-- select * from cte2;

select
  id,
  month,
  salary
from
  cte2
where
  -- If an employee worked only for one month, no output
  (id, month) not in (
    select id, recent_month from cte1
  )
order by
  1,
  2 desc
;
