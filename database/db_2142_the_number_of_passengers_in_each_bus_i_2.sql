# with
# cte1 as (
# select
#   a.bus_id,
#   b.passenger_id,
#   row_number() over(
#     partition by b.passenger_id
#     order by a.arrival_time
#   ) as row_num
# from
#   buses as a,
#   passengers as b
# where
#   a.arrival_time >= b.arrival_time
# ),
# cte2 as (
# select
#   bus_id,
#   count(passenger_id) as passengers_cnt
# from
#   cte1
# where
#   row_num = 1
# group by
#   1
# )

# select
#   a.bus_id,
#   ifnull(b.passengers_cnt, 0) as passengers_cnt
# from
#   buses as a
# left join
#   cte2 as b
# on
#   a.bus_id = b.bus_id
# order by
#   1
# ;

-- Find boarding time of passengers
with cte as (
  select
    b.passenger_id,
    min(a.arrival_time) as boarding_time
  from
    buses as a,
    passengers as b
  where
    b.arrival_time <= a.arrival_time
  group by
    1
)

-- select * from cte;

select
  a.bus_id,
  count(b.passenger_id) as passengers_cnt
from
  buses as a
left join
  cte as b
on
  a.arrival_time = b.boarding_time
group by
  1
order by
  1
;