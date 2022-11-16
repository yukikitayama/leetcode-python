-- Compute confirmation rate by user_id
with cte as (
  select
    user_id,
    -- Average of binary will be rate
    round(avg(if(action = 'confirmed', 1, 0)), 2) as confirmation_rate
  from
    confirmations
  group by
    1
)

select
  a.user_id,
  -- The confirmation rate of a user that did not request any confirmation messages is 0
  -- left join could give us null
  ifnull(b.confirmation_rate, 0) as confirmation_rate
from
  signups as a
left join
  cte as b
on
  a.user_id = b.user_id
;