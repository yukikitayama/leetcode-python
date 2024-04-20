-- Write your PostgreSQL query statement below

with cte as (
  select
    user_id,
    -- integer casting because sum() cannot have boolean argument
    -- decimal casting because we wanna avoid integer division
    sum((action = 'confirmed')::integer)::decimal / count(*) as confirmation_rate
  from
    confirmations
  group by
    1
)

select
  a.user_id,
  round(coalesce(b.confirmation_rate, 0), 2) as confirmation_rate
from
  signups as a
left join
  cte as b
on
  a.user_id = b.user_id
;