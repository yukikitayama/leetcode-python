with
cte1 as (
select
  distinct a.pid as pid_not_location_unique
from
  insurance as a
inner join
  insurance as b
on
  a.lat = b.lat
  and a.lon = b.lon
  and a.pid != b.pid
),

cte2 as (
  select
    distinct c.pid as multiple_same_pid
  from
    insurance as c
  inner join
    insurance as d
  on
    c.tiv_2015 = d.tiv_2015
    and c.pid != d.pid
),

cte3 as (
  select
    tiv_2015
  from
    insurance
  group by
    tiv_2015
  having
    count(*) > 1
),

cte4 as (
  select
    lat,
    lon
  from
    insurance
  group by
    lat,
    lon
  having
    count(*) = 1
)

-- select * from cte1;
-- select * from cte2;
-- select * from cte3;
-- select * from cte4;

# select
#   round(sum(tiv_2016), 2) as tiv_2016
# from
#   insurance
# where
#   pid in (
#     select multiple_same_pid from cte2
#   )
#   and pid not in (
#     select pid_not_location_unique from cte1
#   )

select
  round(sum(tiv_2016), 2) as tiv_2016
from
  insurance
where
  (lat, lon) in (
    select lat, lon from cte4
  )
  and
    tiv_2015 in (
      select tiv_2015 from cte3
    )
;

