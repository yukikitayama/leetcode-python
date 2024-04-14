# Write your MySQL query statement below
with cte as (
  select
    wimbledon as player_id
  from
    championships
  union all
  select
    fr_open as player_id
  from
    championships
  union all
  select
    us_open as player_id
  from
    championships
  union all
  select
    au_open as player_id
  from
    championships
)

select
  a.player_id,
  b.player_name,
  count(a.player_id) as grand_slams_count
from
  cte as a
left join
  players as b
on
  a.player_id = b.player_id
group by
  1,
  2
