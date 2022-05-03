select
  curr.id
from
  weather as curr,
  weather as prev
where
  curr.temperature > prev.temperature
  and datediff(curr.recorddate, prev.recorddate) = 1