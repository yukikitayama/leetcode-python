-- Write your PostgreSQL query statement below
with cte as (
  select
    country,
    winery,
    dense_rank() over(
      partition by country
      order by sum(points) desc, winery
    ) as d_rank,
    concat(winery, ' (', sum(points)::text, ')') as winery_point
  from
    wineries
  group by
    1,
    2
)

-- select * from cte order by country, d_rank;

select
  distinct a.country,
  b.winery_point as top_winery,
  coalesce(c.winery_point, 'No second winery') as second_winery,
  coalesce(d.winery_point, 'No third winery') as third_winery
from
  wineries as a
left join
  (select * from cte where d_rank = 1) as b
on
  a.country = b.country
left join
  (select * from cte where d_rank = 2) as c
on
  a.country = c.country
left join
  (select * from cte where d_rank = 3) as d
on
  a.country = d.country
order by
  1
;