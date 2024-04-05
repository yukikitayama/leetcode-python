# Write your MySQL query statement below
with cte as (
  select
    *,
    max(height) over(order by id) as max_so_far_from_top,
    max(height) over(order by id desc) as max_so_far_from_bottom
  from
    heights
),

cte2 as (
  select
    id,
    height,
    if(
      max_so_far_from_top > max_so_far_from_bottom,
      max_so_far_from_bottom,
      max_so_far_from_top
    ) as max_height
  from
    cte
)

-- select * from cte2 order by id;

select
  sum(max_height - height) as total_trapped_water
from
  cte2
;