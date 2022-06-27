with cte as (
  select
    account_id,
    day,
    amount
  from
    transactions
  where
    type = 'Deposit'
  union all
  select
    account_id,
    day,
    -amount as amount
  from
    transactions
  where
    type = 'Withdraw'
)

# select * from cte;

select
  account_id,
  day,
  -- Compute cumulative sum
  sum(amount) over(partition by account_id order by day) as balance
from
  cte
order by
  account_id, day
;