-- https://dev.mysql.com/doc/refman/8.0/en/with.html#common-table-expressions-recursive
with recursive cte as (
  select
    1 as ids
  union all
  select
    ids + 1
  from
    cte
  where
    ids < (
      select max(customer_id) from customers
    )
)

-- select * from cte;

select
  ids
from
  cte
where
  ids not in (
    select customer_id from customers
  )
;