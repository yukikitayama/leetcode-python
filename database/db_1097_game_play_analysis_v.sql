-- Compute day one retention for each install date
select
  install_date as install_dt,
  count(player_id) as installs,
  round(
    count(next_day) / count(player_id),
    2
  ) as day1_retention
from (
-- By player ID, get install date and the day right after the install date
select
  a.player_id,
  a.install_date,
  b.event_date as next_day
from (
select
  player_id,
  min(event_date) as install_date
from
  activity
group by
  player_id
) as a
left join
  activity as b
on
  a.player_id = b.player_id
  and a.install_date + 1 = b.event_date
) as c
group by
  1
;