with cte as (
  select
    date(day) as day,
    max(amount) as max_amount
  from
    transactions
  group by
    1
)

-- select * from cte;

select
  distinct transaction_id
from
  transactions
where
  (date(day), amount) in (
    select * from cte
  )
order by
  1
;