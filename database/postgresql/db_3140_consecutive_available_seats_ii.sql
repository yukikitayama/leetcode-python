-- Write your PostgreSQL query statement below

-- Assign group ID for each consecutive sequence
with cte as (
  select
    seat_id,
    seat_id - row_number() over(order by seat_id) as group_id
  from
    cinema
  where
    free = 1
  order by
    seat_id
),

-- Find number of consecutive sequence for each group
cte2 as (
  select
    group_id,
    count(*) as consecutive_seats_len
  from
    cte
  group by
    1
),

-- Find group IDs which have the longest consecutive sequence
cte3 as (
  select
    group_id
  from
    cte2
  where
    consecutive_seats_len = (
      select max(consecutive_seats_len) from cte2
    )
)

select
  min(seat_id) as first_seat_id,
  max(seat_id) as last_seat_id,
  count(*) as consecutive_seats_len
from
  cte
where
  group_id in (
    select group_id from cte3
  )
group by
  group_id
;