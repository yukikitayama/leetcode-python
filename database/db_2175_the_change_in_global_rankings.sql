with
-- Get ranking before updating
cte1 as (
  select
    team_id,
    name,
    -- cast(something as signed) to avoid erro of BIGINT UNSIGNED value is out of range
    -- When taking difference later, it can produce negative numbers,
    -- so allow negative minus sign to happen
    cast(rank() over(order by points desc, name) as signed) as ranking_before
  from
    teampoints
),

-- Get ranking after updating
cte2 as (
  select
    a.team_id,
    -- cast(something as signed) to avoid erro of BIGINT UNSIGNED value is out of range
    -- When taking difference later, it can produce negative numbers,
    -- so allow negative minus sign to happen
    cast(rank() over(
      order by a.points + b.points_change desc, name
    ) as signed) as ranking_after
  from
    teampoints as a
  left join
    pointschange as b
  on
    a.team_id = b.team_id
)

select
  cte1.team_id,
  cte1.name,
  -- Compute difference in ranking before and after
  cte1.ranking_before - cte2.ranking_after as rank_diff
from
  cte1
left join
  cte2
on
  cte1.team_id = cte2.team_id
;



