with cte as (
  select
    *,
    -- There are duplicated rows by the same columns information
    -- But this problem counts such purchases as a second purchase within 7 days
    -- Assign IDs to make the following self join work
    row_number() over() as id
  from
    users
)

select
  distinct a.user_id as user_id
from
  cte as a
-- Self-join
join
  cte as b
on
  a.user_id = b.user_id
  -- This can exclude the same purchases, so that we can find the second purchases
  and a.id <> b.id
where
  -- User ABS() because if a.created_at is less than b.created_at by more than 7 days
  -- datediff() <= 7 is true, but that's not what we want
  abs(datediff(a.created_at, b.created_at)) <= 7
;