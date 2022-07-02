-- Use window function

with
cte1 as (
  select
    player_id,
    result,
    match_day,
    row_number() over(partition by player_id order by match_day) as rnk
  from
    matches
),

cte2 as (
  select
    player_id,
    -- This difference will be constant for the range where consecutive wins happen
    rnk - row_number() over(partition by player_id order by match_day) as group_id
  from
    cte1
  where
    result = 'Win'
)

# select * from cte1;
# select * from cte2;

select
  a.player_id,
  ifnull(max(b.cnt), 0) as longest_streak
from (
  select
    distinct player_id
  from
    matches
) as a
left join (
  select
    player_id,
    group_id,
    -- Group by allows us to compute count of consecutive wins by player_id and group_id
    -- group_id is experienced by player_id for wins
    count(*) as cnt
  from
    cte2
  group by
    1,
    2
) as b
on
  a.player_id = b.player_id
group by
  1
;
