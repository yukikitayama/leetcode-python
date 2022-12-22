with cte as (
  select
    *,
    row_number() over(partition by continent order by name) as row_num
  from
    student
)

-- select * from cte;

select
  -- max() to only gets values and nulls, not to get maximum of something
  max(case when continent = 'America' then name else null end) as America,
  max(case when continent = 'Asia' then name else null end) as Asia,
  max(case when continent = 'Europe' then name else null end) as Europe
from
  cte
group by
  row_num
;
