select
  player_id,
  player_name,
  sum(player_id = wimbledon) + sum(player_id = fr_open) + sum(player_id = us_open) + sum(player_id = au_open) as grand_slams_count
from
  players
inner join
  championships
on
  player_id = wimbledon
  or player_id = fr_open
  or player_id = us_open
  or player_id = au_open
group by
  player_id
;