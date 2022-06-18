select
  session_id
from
  playback as a
left join
  ads as b
on
  a.customer_id = b.customer_id
  and b.timestamp between start_time and end_time
where
  b.ad_id is null
;