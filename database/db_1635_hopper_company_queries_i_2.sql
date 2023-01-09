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

-- Active drivers
cte2 as (
  select
    year(join_date) as year,
    month(join_date) as month,
    -- Compute cumulative sum of counts so far as active drivers of each month
    sum(count(driver_id)) over(order by join_date) as cumsum_driver
  from
    drivers
  group by
    1,
    2
),
cte3 as (
  select
    month,
    cumsum_driver
  from
    cte2
  where
    -- We need statistics only in 2020
    year = 2020
),

-- Accepted rides
cte4 as (
  select
    month(b.requested_at) as month,
    count(a.ride_id) as accepted_rides
  from
    acceptedrides as a
  left join
    rides as b
  on
    a.ride_id = b.ride_id
  where
    year(requested_at) = 2020
  group by
    1
)

select
  a.month,
  -- When left join gives us null, first we replace it with 0
  -- then we wanna use the previous cumsum which won't decreas
  -- so take max so far as window function
  max(ifnull(b.cumsum_driver, 0)) over(order by a.month) as active_drivers,
  ifnull(c.accepted_rides, 0) as accepted_rides
from
  cte1 as a
left join
  cte3 as b
on
  a.month = b.month
left join
  cte4 as c
on
  a.month = c.month
order by
  1
;
