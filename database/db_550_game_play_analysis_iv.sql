select
  # No consecutive 2 days played player id is null
  round(count(b.player_id) / count(a.player_id), 2) as fraction
from
(
select
  player_id,
  min(event_date) as first_login
from
  activity
group by
  player_id
) as a
left join
  activity as b
on
  a.first_login = b.event_date - 1
  and a.player_id = b.player_id
