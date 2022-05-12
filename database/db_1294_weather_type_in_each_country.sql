select
  b.country_name,
  case
    when avg(weather_state) <= 15 then 'Cold'
    when avg(weather_state) >= 25 then 'Hot'
    else 'Warm'
  end as weather_type
from
  weather as a
left join
  countries as b
on
  a.country_id = b.country_id
where
  year(a.day) = 2019
  and month(a.day) = 11
group by
  b.country_name
;