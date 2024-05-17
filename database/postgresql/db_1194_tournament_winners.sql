/*
Union first player with score and second player with score
Compute total score for each player id
Join the total score to players table
Assign rank by descending score within group id
Return rank 1 for each group

| group_id | player_id |
| -------- | --------- |
| 1        | 15        |
| 2        | 10        | <- 35
| 3        | 40        |...
*/


-- Write your PostgreSQL query statement below

with cte as (
  select
    first_player as player_id,
    first_score as score
  from
    matches
  union all
  select
    second_player as player_id,
    second_score as score
  from
    matches
),

cte2 as (
  select
    player_id,
    sum(score) as total_score
  from
    cte
  group by
    1
),

cte3 as (
  select
    a.group_id,
    a.player_id,
    rank() over(
      partition by a.group_id
      -- coalesce because null will be assigned highest rank
      order by coalesce(b.total_score, 0) desc, a.player_id
    ) as rank
  from
    players as a
  left join
    cte2 as b
  on
    a.player_id = b.player_id
)

-- select * from cte2;
-- select * from cte3;

select
  group_id,
  player_id
from
  cte3
where
  rank = 1
;