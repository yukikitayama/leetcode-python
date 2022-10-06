with cte as (
-- Score when a team is host
select
  host_team as team_id,
  case
    when host_goals > guest_goals then 3
    when host_goals = guest_goals then 1
    else 0
  end as score
from
  matches

union all

-- Score when a team is guest
select
  guest_team as team_id,
  case
    when guest_goals > host_goals then 3
    when guest_goals = host_goals then 1
    else 0
  end as score
from
 matches
)

select
  a.team_id,
  a.team_name,
  -- Score is null when a team didn't have a match
  -- null happens by left join, but the problem requires us to return 0
  ifnull(sum(b.score), 0) as num_points
from
  teams as a
left join
  cte as b
on
  a.team_id = b.team_id
group by
  1
order by
  3 desc,
  1
;