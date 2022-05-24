-- Find first call by date
-- Find last call by date

with

cte1 as (
  select
    caller_id as user_id,
    call_time,
    recipient_id
  from
    calls

  union

  select
    recipient_id as user_id,
    call_time,
    caller_id as recipient_id
  from
    calls
),

cte2 as (
  select
    user_id,
    recipient_id,
    date(call_time) as day,
    dense_rank() over(
      partition by user_id, date(call_time)
      order by call_time
    ) as first_call,
    dense_rank() over(
      partition by user_id, date(call_time)
      order by call_time desc
    ) as last_call
  from
    cte1
)

select
  distinct user_id
from
  cte2
where
  first_call = 1 or last_call = 1
group by
  user_id, day
having
  count(distinct recipient_id) = 1
;