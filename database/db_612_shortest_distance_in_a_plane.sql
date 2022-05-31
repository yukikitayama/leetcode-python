select
  round(sqrt(power(b.x - a.x, 2) + power(b.y - a.y, 2)), 2) as shortest
from
  point2d as a,
  point2d as b
where
  a.x != b.x
  or a.y != b.y
order by
  shortest
limit
  1
;
