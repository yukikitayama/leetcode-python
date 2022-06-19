# -- Version 1
# with
# cte1 as (
# -- matches_played, goal_for, goal_agaist
# select
#   a.team_id,
#   count(*) as matches_played,
#   sum(a.score_for) as goal_for,
#   sum(a.score_against) as goal_against
# from (
# select
#   home_team_id as team_id,
#   home_team_goals as score_for,
#   away_team_goals as score_against
# from
#   matches
# union all
# select
#   away_team_id as team_id,
#   away_team_goals as score_for,
#   home_team_goals as score_against
# from
#   matches
# ) as a
# group by
#   1
# ),

# cte2 as (
# -- points
# select
#   b.team_id,
#   sum(b.points) as points
# from (
# select
#   home_team_id as team_id,
#   case
#     when home_team_goals > away_team_goals then 3
#     when home_team_goals = away_team_goals then 1
#     else 0
#   end as points
# from
#   matches
# union all
# select
#   away_team_id as team_id,
#   case
#     when away_team_goals > home_team_goals then 3
#     when away_team_goals = home_team_goals then 1
#     else 0
#   end as points
# from
#   matches
# ) as b
# group by
#   1
# )

# select
#   c.team_name,
#   d.matches_played,
#   e.points,
#   d.goal_for,
#   d.goal_against,
#   d.goal_for - d.goal_against as goal_diff
# from
#   cte1 as d
# left join
#   teams as c
# on
#   c.team_id = d.team_id
# left join
#   cte2 as e
# on
#   c.team_id = e.team_id
# order by
#   3 desc,
#   6 desc,
#   1


-- Version 2
select
  b.team_name,
  count(*) as matches_played,
  sum(case
    when home_team_goals > away_team_goals then 3
    when home_team_goals = away_team_goals then 1
    else 0
  end) as points,
  sum(home_team_goals) as goal_for,
  sum(away_team_goals) as goal_against,
  sum(home_team_goals) - sum(away_team_goals) as goal_diff
from (
select
  home_team_id as home_team_id,
  home_team_goals as home_team_goals,
  away_team_goals as away_team_goals
from
  matches
union all
select
  away_team_id as home_team_id,
  away_team_goals as home_team_goals,
  home_team_goals as away_team_goals
from
  matches
) as a
left join
  teams as b
on
  a.home_team_id = b.team_id
group by
  1
order by
  3 desc,
  6 desc,
  1


;
