/*
Actually doesn't have to be consecutive
find the data whose start and other data whose end is within 12 hours
*/

-- Write your PostgreSQL query statement below

select
  distinct a.user_id
from
  sessions as a
join
  sessions as b
on
  a.user_id = b.user_id
  and a.session_type = b.session_type
  and a.session_start > b.session_start
  and date_part('day', a.session_start - b.session_end) * 24 + date_part('hour', a.session_start - b.session_end) <= 12
order by
  1
;
