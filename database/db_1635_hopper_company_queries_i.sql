# -- Make month table
# select 1 as month
# union select 2 as month
# union select 3 as month
# union select 4 as month
# union select 5 as month
# union select 6 as month
# union select 7 as month
# union select 8 as month
# union select 9 as month
# union select 10 as month
# union select 11 as month
# union select 12 as month

# -- Generate driver table
# select
#   driver_id,
#   case
#     when year(join_date) = 2019 then '1'
#     else month(join_date)
#   end as 'month'
# from
#   drivers
# where
#   -- <= 2020 because we wanna know the status in 2020
#   year(join_date) <= 2020

# -- Generate accepted ride table
# select
#   month(b.requested_at) as 'month',
#   a.ride_id
# from
#   acceptedrides as a
# join
#   rides as b
# on
#   a.ride_id = b.ride_id
# where
#   year(b.requested_at) = 2020

-- Combine them
select
  c.month,
  count(distinct d.driver_id) as active_drivers,
  count(distinct e.ride_id) as accepted_rides
from (
select 1 as month
union select 2 as month
union select 3 as month
union select 4 as month
union select 5 as month
union select 6 as month
union select 7 as month
union select 8 as month
union select 9 as month
union select 10 as month
union select 11 as month
union select 12 as month
) as c
-- Join the driver table
left join (
select
  driver_id,
  case
    when year(join_date) = 2019 then '1'
    else month(join_date)
  end as 'month'
from
  drivers
where
  -- <= 2020 because we wanna know the status in 2020
  year(join_date) <= 2020
) as d
on
  -- Use >= because we wanna get cumulative sum, which will be computed
  -- later by group by
  c.month >= d.month
-- Join the accepted ride table
left join (
select
  month(b.requested_at) as 'month',
  a.ride_id
from
  acceptedrides as a
join
  rides as b
on
  a.ride_id = b.ride_id
where
  year(b.requested_at) = 2020
) as e
on
  c.month = e.month
group by
  c.month
order by
  c.month

;



