-- Use common table expression because the same subquery table is used twice
-- Find total score by player_id
with cte as (
select
  a.player,
  sum(a.score) as total_score
from (
select
  first_player as player,
  first_score as score
from
  matches
-- Use UNION ALL because we will have duplicated records, and UNION removes them, but
-- it will affect sum of scores
union all
select
  second_player as player,
  second_score as score
from
  matches
) as a
group by
  a.player
)

select
  d.group_id,
  min(d.player_id) as player_id
from
  players as d
left join
  cte as e
on
  d.player_id = e.player
where
  (d.group_id, e.total_score) in (
-- Compute highest total score by group_id
select
  b.group_id,
  max(c.total_score)
from
  players as b
left join
  cte as c
on
  b.player_id = c.player
group by
  b.group_id
  )
group by
  d.group_id
;
