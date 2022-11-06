
with
cte1 as (
  select
    wimbledon as winner
  from
    championships
  union all
  select
    fr_open as winner
  from
    championships
  union all
  select
    us_open as winner
  from
    championships
  union all
  select
    au_open as winner
  from
    championships
),
cte2 as (
  select
    winner,
    count(*) as grand_slams_count
  from
    cte1
  group by
    1
)

select
  a.winner as player_id,
  b.player_name,
  a.grand_slams_count
from
  cte2 as a
left join
  players as b
on
  a.winner = b.player_id
;