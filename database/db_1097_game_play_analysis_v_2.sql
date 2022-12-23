with
-- Install date by player
cte1 as (
  select
    player_id,
    min(event_date) as install_dt
  from
    activity
  group by
    1
),
-- Players who retained by coming back next day and their install date
cte2 as (
  select
    a.player_id,
    a.install_dt
  from
    cte1 as a
  left join
    activity as b
  on
    a.player_id = b.player_id
    -- and a.install_dt + 1 = b.event_date
    and a.install_dt = date_sub(b.event_date, interval 1 day)
  where
    b.event_date is not null
),
-- Count number of retantions by each install date
cte3 as (
  select
    install_dt,
    count(player_id) as retentions
  from
    cte2
  group by
    1
)

-- select * from cte1;
-- select * from cte2;
-- select * from cte3;

select
  a.install_dt,
  count(a.player_id) as installs,
  round(ifnull(b.retentions, 0) / count(a.player_id), 2) as "Day1_retention"
from
  cte1 as a
left join
  cte3 as b
on
  a.install_dt = b.install_dt
group by
  1
;
