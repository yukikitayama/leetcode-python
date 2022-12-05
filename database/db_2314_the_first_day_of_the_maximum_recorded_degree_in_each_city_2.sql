with cte as (
  select
    *,
    row_number() over(
      partition by city_id
      order by degree desc, day
    ) as row_num
  from
    weather
)

select
  city_id,
  day,
  degree
from
  cte
where
  row_num = 1
order by
  1
;
