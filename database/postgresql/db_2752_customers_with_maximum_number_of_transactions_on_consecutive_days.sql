-- Write your PostgreSQL query statement below
with cte as (
  select
    *,
    -- To create group by within customer_id, find first transaction date for each customer to compute difference in days
    date_part('day', transaction_date::timestamp - (min(transaction_date) over(partition by customer_id))::timestamp) + 1 as diff_day,
    -- row_num increments regardless of skip in transaction dates but diff day skip when no transaction, so we can make group ID for each consecutive days as group
    row_number() over(partition by customer_id order by transaction_date) as row_num
  from
    transactions
),

cte2 as (
  select
    customer_id,
    transaction_date,
    diff_day - row_num as group_id
  from
    cte
),

cte3 as (
  select
    customer_id,
    group_id,
    count(transaction_date) as num_consecutive_transaction
  from
    cte2
  group by
    1,
    2
)

-- select * from cte2 order by 1, 2;
-- select * from cte3;

select
  -- distinct customer_id <- this should be correct
  customer_id
from
  cte3
where
  num_consecutive_transaction = (
    select max(num_consecutive_transaction) from cte3
  )
order by
  1
;
