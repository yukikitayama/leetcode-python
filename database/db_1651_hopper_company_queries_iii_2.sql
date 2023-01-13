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

-- Compute total ride distance and total ride duration by month in 2020
cte2 as (
  select
    month(b.requested_at) as month,
    sum(a.ride_distance) as total_ride_distance,
    sum(a.ride_duration) as total_ride_duration
  from
    acceptedrides as a
  left join
    rides as b
  on
    a.ride_id = b.ride_id
  where
    year(b.requested_at) = 2020
  group by
    1
),

-- Merge
cte3 as (
  select
    a.month,
    ifnull(b.total_ride_distance, 0) as total_ride_distance,
    ifnull(b.total_ride_duration, 0) as total_ride_duration
  from
    cte1 as a
  left join
    cte2 as b
  on
    a.month = b.month
),

-- Compute average ride distance and duration of every 3-month window upto October
cte4 as (
  select
    a.month,
    round(
      (a.total_ride_distance + ifnull(b.total_ride_distance, 0) + ifnull(c.total_ride_distance, 0)) / 3,
      2
    ) as average_ride_distance,
    round(
      (a.total_ride_duration + ifnull(b.total_ride_duration, 0) + ifnull(c.total_ride_duration, 0)) / 3,
      2
    ) as average_ride_duration
  from
    cte3 as a
  left join
    cte3 as b
  on
    a.month = b.month - 1
  left join
    cte3 as c
  on
    a.month = c.month - 2
  where
    a.month <= 10
)

-- select * from cte1;
-- select * from cte2;
-- select * from cte3;
select * from cte4;
