# -- Month table
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

# -- Drivers that accepted at least one ride during the month
# select
#   month(b.requested_at) as month,
#   count(distinct a.driver_id) as accepted_driver
# from
#   acceptedrides as a
# left join
#   rides as b
# on
#   a.ride_id = b.ride_id
# where
#   year(b.requested_at) = 2020
# group by
#   1

# -- Available drivers during the month
# select
#   case
#     when year(join_date) = 2019 then 1
#     else month(join_date)
#   end as month,
#   count(driver_id) as available_driver
# from
#   drivers
# where
#   year(join_date) <= 2020
# group by
#   1

with cte1 as (
-- Month table
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
), cte2 as (
-- Drivers that accepted at least one ride during the month
select
  month(b.requested_at) as month,
  count(distinct a.driver_id) as accepted_driver
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
), cte3 as (
select
  case
    when year(join_date) = 2019 then 1
    else month(join_date)
  end as month,
  count(driver_id) as available_driver
from
  drivers
where
  year(join_date) <= 2020
group by
  1
)

select
  cte1.month,
  round(100 * ifnull(cte2.accepted_driver / sum(cte3.available_driver), 0), 2) as working_percentage
from
  cte1
left join
  cte3
on
  -- >= because drivers cumulatively increase each month
  cte1.month >= cte3.month
left join
  cte2
on
  cte1.month = cte2.month
group by
  1
order by
  1
;
