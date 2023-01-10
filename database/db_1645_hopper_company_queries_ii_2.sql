with recursive

-- Month table
cte1 as (
  select
    1 as month
  union all
  select
    month + 1 as month
  from
    cte1
  where
    month < 12
),

-- Drivers that accepted at least one ride during the month
cte2 as (
  select
    month(a.requested_at) as month,
    count(distinct b.driver_id) as driver_count
  from
    rides as a
  left join
    acceptedrides as b
  on
    a.ride_id = b.ride_id
  where
    year(a.requested_at) = 2020
    and b.driver_id is not null
  group by
    1
),

-- Available drivers during the month
cte3 as (
  select
    year(join_date) as year,
    month(join_date) as month,
    -- Compute cumulative sum of drivers up to the end of 2020
    sum(count(driver_id)) over(order by join_date) as cumsum_driver
  from
    drivers
  where
    year(join_date) <= 2020
  group by
    1,
    2
),
cte4 as (
  select
    a.month,
    -- When a certain month is missing, left join gives us null, so fill them with 0
    -- and we need to recompute the available driver count so far, so replace 0 with the current max
    max(ifnull(b.cumsum_driver, 0)) over(order by a.month) available_driver
  from
    cte1 as a
  left join
    (select * from cte3 where year = 2020) as b
  on
    a.month = b.month
  group by
    1
)

-- Aggregate all as answer output
select
  a.month,
  if(
    -- If there is no drivers who accepted ride, working percentage is 0
    b.driver_count is null,
    0,
    -- Otherwise compute working percentage by a given formula
    round(b.driver_count / a.available_driver * 100, 2)
  ) as working_percentage
from
  cte4 as a
left join
  cte2 as b
on
  a.month = b.month
;
