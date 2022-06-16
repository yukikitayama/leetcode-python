-- Create month table
with recursive month as (
  select
    1 as month
  union
  select
    month + 1 as month
  from
    month
  where
    month < 12
),

-- Monthly total ride distance, and total ride duration
month_rides as (
  select
    month(a.requested_at) as month,
    sum(b.ride_distance) as ride_distance,
    sum(b.ride_duration) as ride_duration
  from
    rides as a
  join
    acceptedrides as b
  on
    a.ride_id = b.ride_id
  where
    year(a.requested_at) = 2020
  group by
    1
),

-- Create monthly clean table
every_month_rides as (
  select
    a.month,
    ifnull(b.ride_distance, 0) as ride_distance,
    ifnull(b.ride_duration, 0) as ride_duration
  from
    month as a
  left join
    month_rides as b
  on
    a.month = b.month
)

# select * from month;
# select * from month_rides;
# select * from every_month_rides;

-- Self-join 3 times to get every 3-month window
select
  a.month as month,
  round((a.ride_distance + b.ride_distance + c.ride_distance) / 3, 2) as average_ride_distance,
  round((a.ride_duration + b.ride_duration + c.ride_duration) / 3, 2) as average_ride_duration
from
  every_month_rides as a
join
  every_month_rides as b
on
  a.month = b.month - 1
join
  every_month_rides as c
on
  b.month = c.month - 1

;