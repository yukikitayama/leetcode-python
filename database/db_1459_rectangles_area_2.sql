select
  a.id as p1,
  b.id as p2,
  abs(a.x_value - b.x_value) * abs(a.y_value - b.y_value) as area
from
  points as a,
  points as b
where
  a.x_value != b.x_value
  and a.y_value != b.y_value
  and a.id < b.id
order by
  3 desc,
  1,
  2
;
