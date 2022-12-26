with
-- Stack table
cte1 as (
  select
    first_player as player,
    first_score as score
  from
    matches
  union all
  select
    second_player as player,
    second_score as core
  from
    matches
),
-- Compute total score by each player
cte2 as (
  select
    player,
    sum(score) as total_score
  from
    cte1
  group by
    1
),
-- Assign order by total score and player ID
cte3 as (
  select
    a.player_id,
    a.group_id,
    row_number() over(
      partition by group_id
      -- In the case of a tie, the lowest player_id wins
      order by total_score desc, player_id
    ) as row_num
  from
    players as a
  left join
    cte2 as b
  on
    a.player_id = b.player
  group by
    1
)

-- select * from cte2;
-- select * from cte3;

select
  group_id,
  player_id
from
  cte3
where
  row_num = 1
;
