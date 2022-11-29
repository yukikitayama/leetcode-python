with cte as (
  select
    a.team_id,
    a.name,
    cast(rank() over(order by points desc, a.name) as signed) as old_rank,
    cast(rank() over(order by a.points + b.points_change desc, a.name) as signed) as new_rank
  from
    teampoints as a
  left join
    pointschange as b
  on
    a.team_id = b.team_id
)

-- select * from cte;

select
  team_id,
  name,
  old_rank - new_rank as rank_diff
from
  cte
;