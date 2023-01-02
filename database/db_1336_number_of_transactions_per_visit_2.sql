with recursive
cte1 as (
  select
    a.user_id,
    a.visit_date,
    b.transaction_date,
    b.amount
  from
    visits as a
  left join
    transactions as b
  on
    a.user_id = b.user_id
    and a.visit_date = b.transaction_date
),
cte2 as (
  select
    user_id,
    visit_date,
    transaction_date,
    if(transaction_date is null, 0, count(*)) as transactions_count
  from
    cte1
  group by
    1,
    2,
    3
),
cte3 as (
  select
    transactions_count,
    count(*) as visits_count
  from
    cte2
  group by
    1
),
-- Create visits count table
cte4 as (
  select
    0 as transactions_count
  union all
  select
    transactions_count + 1
  from
    cte4
  where
    transactions_count < (
      select max(transactions_count) from cte3
    )
)

-- select * from cte1 order by user_id, visit_date, transaction_date;
-- select * from cte2;
-- select * from cte3;
-- select * from cte4;

select
  a.transactions_count,
  ifnull(b.visits_count, 0) as visits_count
from
  cte4 as a
left join
  cte3 as b
on
  a.transactions_count = b.transactions_count
order by
  1
;