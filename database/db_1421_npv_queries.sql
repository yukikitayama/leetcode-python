select
  q.id,
  q.year,
  ifnull(n.npv, 0) as npv
from
  queries as q
left join
  npv as n
on
  q.id = n.id
  and q.year = n.year