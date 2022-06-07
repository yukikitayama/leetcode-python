-- Put recursive right after WITH
with recursive
-- This is not recursive
-- Compute transaction counts by user_id and visit_date
cte as (
select
  a.user_id,
  a.visit_date,
  count(b.amount) as transactions_count
from
  visits as a
left join
  transactions as b
on
  a.user_id = b.user_id
  and a.visit_date = b.transaction_date
group by
  1,
  2
),
-- This is recursive
-- CTE to create a sequence of numbers to create a list of transaction counts
numbers as (
  select
    0 as num
  union all
  select
    num + 1
  from
    numbers
  where
    num < (
      select
        max(transactions_count) as max_transactions_count
      from
        cte
    )
)

select
  num as transactions_count,
  ifnull(b.visits_count, 0) as visits_count
from
  numbers as a
left join (
-- Count how many those transactions_count exist by transaction count
select
  transactions_count,
  count(user_id) as visits_count
from
  cte
group by
  transactions_count
) as b
on
  a.num = b.transactions_count
order by
  transactions_count
;
