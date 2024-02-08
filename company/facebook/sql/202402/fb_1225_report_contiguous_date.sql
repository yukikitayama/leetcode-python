-- Write your PostgreSQL query statement below

/*
Union table
group successive success/fail date
  compute min date and max date within group

group id
  order by date, partition by s/f status assing row number
  difference between date and row number
    same group has constant




start: min(date)
end: max(date)

eg
  1/1 success 1
  1/2 success 2
  1/3 success 3
  1/4 fail    1
  1/5 fail    2
  1/6 success 4
*/

with cte as (
  select
    'succeeded' as period_state,
    success_date as d
  from
    succeeded
  union
  select
    'failed' as period_state,
    fail_date as d
  from
    failed
),

cte2 as (
  select
    *,
    -- row_number() over(
    --   partition by period_state
    --   order by d
    -- ) as row_num_by_period_date,
    -- row_number() over(
    --   order by d
    -- ) as row_num_by_date
    row_number() over(
      order by d
    ) - row_number() over(
      partition by period_state
      order by d
    ) as group_id
  from
    cte
)

-- select * from cte2 order by d;

select
  period_state,
  min(d) as start_date,
  max(d) as end_date
from
  cte2
where
  d between '2019-01-01'::date and '2019-12-31'::date
group by
  -- period_state needs to be in group by statement, otherwise PostgreSQL throws error
  period_state,
  group_id
order by
  start_date
;


