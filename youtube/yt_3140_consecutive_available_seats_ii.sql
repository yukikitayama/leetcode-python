/*
seat_id free row_number diff(seat_id - row num)
1 1 1 0
2 0 1 1
3 1 2 1
4 1 3 1
5 1 4 1
6 0 2 4
7 1 5 2
8 1 6 2
9 1 7 2
*/

-- Write your PostgreSQL query statement below
with cte as (
  select
    seat_id,
    seat_id - row_number() over(partition by free order by seat_id) as group_id
  from
    cinema
  where
    free = 1
),

cte2 as (
  select
    group_id,
    count(*) as num_consecutive_seat
  from
    cte
  group by
    1
),

cte3 as (
  select
    group_id
  from
    cte2
  where
    num_consecutive_seat = (
      select max(num_consecutive_seat) from cte2
    )
)

-- select * from cte;
-- select * from cte3;

select
  min(seat_id) as first_seat_id,
  max(seat_id) as last_seat_id,
  max(seat_id) - min(seat_id) + 1 as consecutive_seats_len
from
  cte
where
  group_id in (
    select group_id from cte3
  )
group by
  group_id
order by
  1
;
