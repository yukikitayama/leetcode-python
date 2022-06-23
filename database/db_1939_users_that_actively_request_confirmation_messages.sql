select
  distinct a.user_id
from
  confirmations as a
join
  confirmations as b
on
  a.user_id = b.user_id
  and a.time_stamp > b.time_stamp
  and timestampdiff(second, b.time_stamp, a.time_stamp) <= 60 * 60 * 24
;
