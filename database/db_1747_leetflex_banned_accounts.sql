select
#   a.account_id,
#   a.ip_address,
#   a.login,
#   a.logout
  distinct a.account_id
from
  loginfo as a,
  loginfo as b
where
  a.login between b.login and b.logout
  and a.account_id = b.account_id
  and a.ip_address != b.ip_address
;