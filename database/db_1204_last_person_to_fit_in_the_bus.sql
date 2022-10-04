-- Use CTE to avoid having nested query
with cte as (
  select
    *,
    -- Compute cumulative sum of weight order by turn
    sum(weight) over(order by turn) as cumsum
  from
    queue
)

select
  person_name
from
  cte
-- Limit only people who can take the bus
where
  cumsum <= 1000
-- Using order by and limit together to show only the last person
order by
  cumsum desc
limit
  1
;