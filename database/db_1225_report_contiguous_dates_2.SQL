with
-- Stack tables for convenience
-- Also fiter the rows in the required date range
cte1 as (
  select
    'failed' as period_state,
    fail_date as date
  from
    failed
  where
    fail_date between '2019-01-01' and '2019-12-31'
  union all
  select
    'succeeded' as period_state,
    success_date as date
  from
    succeeded
  where
    success_date between '2019-01-01' and '2019-12-31'
),
-- row_number() over(order by date) is ID which keeps incrementing in each row by ascending date
-- row_number() over(partition by period_state order by date) is ID only incremented within each period_state
-- When taking difference between the IDs, the difference remain the same within period_state and consecutive second IDs
-- So the difference works as group ID, with which eventually we aggregate.
cte2 as (
  select
    *,
    row_number() over(order by date) - row_number() over(partition by period_state order by date) as group_id
  from
    cte1
)

select
  period_state,
  min(date) as start_date,
  max(date) as end_date
from
  cte2
group by
  period_state,
  group_id
order by
  2
;
