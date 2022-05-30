select
  round(sum(a.tiv_2016), 2) as tiv_2016
from
  insurance as a
where
  -- tiv_2015 is not unique
  a.tiv_2015 in (
    select
      tiv_2015
    from
      insurance
    group by
      tiv_2015
    having
      count(*) > 1
  )
  -- But lat and lon are unique
  and (lat, lon) in (
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
;
