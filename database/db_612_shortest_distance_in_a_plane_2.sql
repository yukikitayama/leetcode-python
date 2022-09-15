select
  round(min(sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))), 2) as shortest
from
  point2d as a,
  point2d as b
where
  a.x != b.x
  or a.y != b.y
;
