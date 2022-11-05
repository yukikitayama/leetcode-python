select
  distinct a.account_id
from
  loginfo as a,
  loginfo as b
where
  a.account_id = b.account_id
  and a.ip_address != b.ip_address
  and (
    a.logout between b.login and b.logout
    or b.login between a.login and a.logout
  )
;
