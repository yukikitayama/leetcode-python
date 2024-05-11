-- Write your PostgreSQL query statement below

-- Find increasing amount
with cte as (
  select
    a.customer_id,
    a.transaction_date
  from
    transactions as a
  join
    transactions as b
  on
    a.customer_id = b.customer_id
    and b.amount > a.amount
    and date_part('day', b.transaction_date::timestamp - a.transaction_date::timestamp) = 1
),

-- Find group ID
cte2 as (
  select
    customer_id,
    transaction_date,
    row_number() over(partition by customer_id order by transaction_date) - (transaction_date - min(transaction_date) over(partition by customer_id)) as group_id
  from
    cte
),

-- Find number of consecutive transactions for at least 3
cte3 as (
  select
    customer_id,
    group_id,
    min(transaction_date) as consecutive_start,
    count(*) as num_following_consecutive_transactions
  from
    cte2
  group by
    1,
    2
)

-- select * from cte order by 1, 2;
-- select * from cte2 order by 1, 2;
-- select * from cte3 order by 1, 2;

select
  customer_id,
  consecutive_start,
  -- Either way
--   (consecutive_start + (num_following_consecutive_transactions || ' days')::interval)::date as consecutive_end
  (consecutive_start + num_following_consecutive_transactions * interval '1 day')::date as consecutive_end
from
  cte3
where
  num_following_consecutive_transactions >= 2
order by
  1,
  2
;