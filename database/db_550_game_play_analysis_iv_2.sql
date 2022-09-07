with
-- First login date by player
cte1 as (
select
  a.player_id,
  min(a.event_date) as first_date
from
  activity as a
group by
  1
)

select
  round(count(c.player_id) / count(b.player_id), 2) as fraction
from
  cte1 as b
left join
  activity as c
on
  b.player_id = c.player_id
  and datediff(c.event_date, b.first_date) = 1