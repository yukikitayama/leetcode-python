select
  distinct a.num as ConsecutiveNums
from
  logs as a,
  logs as b,
  logs as c
where
  a.id = b.id - 1
  and b.id = c.id - 1
  and a.num = b.num
  and b.num = c.num
;
