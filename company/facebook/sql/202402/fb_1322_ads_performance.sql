with cte as (
  select
    ad_id,
    sum(case when action = 'Clicked' then 1 else 0 end) as click,
    sum(case when action = 'Viewed' then 1 else 0 end) as view
  from
    ads
  group by
    1
)

-- select * from cte;

select
  ad_id,
  case
    when click = 0 then 0
    else round(click::decimal / (click + view) * 100, 2)
  end as ctr
from
  cte
order by
  2 desc,
  1
;

