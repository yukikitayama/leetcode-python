/*
host_team guest_team host_goals guest_goals
10        20         3          0

cte
host_team host_goals guest_goals
10        3          0
20        0          3
*/


-- Write your PostgreSQL query statement below
with cte as (
  select
    host_team,
    host_goals,
    guest_goals
  from
    matches
  union all
  select
    guest_team,
    guest_goals,
    host_goals
  from
    matches
)

select
  a.team_id,
  a.team_name,
  coalesce(sum(case
    when b.host_goals > guest_goals then 3
    when b.host_goals = guest_goals then 1
    else 0
  end
  ), 0) as num_points
from
  teams as a
left join
  cte as b
on
  a.team_id = b.host_team
group by
  1,
  2
order by
  3 desc,
  1
;

