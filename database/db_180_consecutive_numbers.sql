select
  distinct a.num as consecutivenums
from
  logs as a,
  logs as b,
  logs as c
where
  a.id = b.id - 1
  and a.id = c.id - 2
  and a.num = b.num
  and a.num = c.num
