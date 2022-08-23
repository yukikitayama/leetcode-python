-- The 3rd CTE uses recursion
with recursive
-- Get the arrival time of a previous bus
-- If no previous bus, arrival time is -999
cte1 as (
  select
    row_number() over(order by arrival_time) as rn,
    bus_id,
    arrival_time,
    lag(arrival_time, 1, -999) over(order by arrival_time) as prev_time,
    capacity
  from
    buses
),

-- Get how many people a current bus should take, without thinking of the remaining passengers from a previous bus
cte2 as (
  select
    a.rn,
    a.bus_id,
    a.capacity,
    count(b.passenger_id) as curr_passenger_cnt
  from
    cte1 as a
  left join
    passengers as b
  on
    a.prev_time < b.arrival_time
    and b.arrival_time <= a.arrival_time
  group by
    1,
    2,
    3
),

-- Get how many people a previous bus wasn't able to take, and how many people a current bus can take
-- This is recursive CTE
cte3 as (
  -- For the first bus
  select
    rn,
    bus_id,
    capacity,
    curr_passenger_cnt,
    case
      when curr_passenger_cnt - capacity <= 0 then 0
      else curr_passenger_cnt - capacity
    end as accumulated_remaining
  from
    cte2
  where
    rn = 1

  union all

  -- For the rest of the buses
  select
    d.rn,
    d.bus_id,
    d.capacity,
    -- cte3 as c works as the previous data, so previous remaining + current passenger
    -- is the number of passenger that a current bus can take
    d.curr_passenger_cnt + c.accumulated_remaining as curr_passenger_cnt,
    case
      when d.curr_passenger_cnt + c.accumulated_remaining - d.capacity <= 0 then 0
      else d.curr_passenger_cnt + c.accumulated_remaining - d.capacity
    end as accumulated_remaining
  from
    cte3 as c
  inner join
    cte2 as d
  -- Recursive CTE work as previous data
  on
    c.rn + 1 = d.rn
)

# select * from cte1;
# select * from cte2;
# select * from cte3;

select
  bus_id,
  case
    when accumulated_remaining > 0 then capacity
    else curr_passenger_cnt
  end as passengers_cnt
from
  cte3
order by
  bus_id
;
