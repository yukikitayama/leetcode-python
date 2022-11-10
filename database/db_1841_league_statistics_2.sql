with
cte1 as (
  select
    home_team_id,
    away_team_id,
    home_team_goals,
    away_team_goals
  from
    matches
  union all
  select
    away_team_id as home_team_id,
    home_team_id as away_team_id,
    away_team_goals as home_team_goals,
    home_team_goals as away_team_goals
  from
    matches
)

select
  a.team_name,
  count(b.home_team_id) as matches_played,
  sum(case
    when b.home_team_goals > b.away_team_goals then 3
    when b.home_team_goals = b.away_team_goals then 1
    else 0
  end) as points,
  sum(b.home_team_goals) as goal_for,
  sum(b.away_team_goals) as goal_against,
  sum(b.home_team_goals) - sum(b.away_team_goals) as goal_diff
from
  teams as a
right join
  cte1 as b
on
  a.team_id = b.home_team_id
group by
  1
order by
  3 desc,
  6 desc,
  1
;