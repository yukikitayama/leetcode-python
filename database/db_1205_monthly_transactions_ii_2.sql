-- Union chargebacks table to be able to show chargebacks month in the output table
with cte as (
  -- Chargeback
  select
    left(a.trans_date, 7) as month,
    b.country,
    -- Create a temporary column to be table to if statement later
    "chargeback" as state,
    b.amount
  from
    chargebacks as a
  inner join
    transactions as b
  on
    a.trans_id = b.id

  union all

  -- Approved
  select
    left(trans_date, 7) as month,
    country,
    state,
    amount
  from
    transactions
  where
    state = "approved"
)

select
  month,
  country,
  sum(if(state = "approved", 1, 0)) as approved_count,
  sum(if(state = "approved", amount, 0)) as approved_amount,
  sum(if(state = "chargeback", 1, 0)) as chargeback_count,
  sum(if(state = "chargeback", amount, 0)) as chargeback_amount
from
  cte
group by
  1,
  2
;