with
-- Transform transaction table to make group by sum
cte1 as (
  select
    paid_by as user_id,
    -amount as amount
  from
    transactions
  -- Use union all instead of union, because we wanna keep duplicate transactions
  -- e.g. If there are 2 transactions of [paid_by: 1, paid_to: 2, amount: 100]
  -- then sum(amount) should be 200, but just UNION will remove one row
  union all
  select
    paid_to as user_id,
    amount
  from
    transactions
),
-- Compute amount change by user_id
cte2 as (
  select
    user_id,
    sum(amount) as delta
  from
    cte1
  group by
    1
)

select
  a.user_id,
  a.user_name,
  -- When no transaction, left join returns null delta column,
  -- but number + null returns null in SQL,
  -- so replace null with 0 to allow summation
  a.credit + ifnull(b.delta, 0) as credit,
  if(a.credit + ifnull(b.delta, 0) < 0, 'Yes', 'No') as credit_limit_breached
from
  users as a
left join
  cte2 as b
on
  a.user_id = b.user_id
;
