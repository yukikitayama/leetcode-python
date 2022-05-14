# Write your MySQL query statement below
select
  # a.id,
  # a.x_value,
  # a.y_value,
  # b.id,
  # b.x_value,
  # b.y_value
  a.id as p1,
  b.id as p2,
  abs(a.x_value - b.x_value) * abs(a.y_value - b.y_value) as area
from
  points as a
join
  points as b
on
  a.x_value != b.x_value
  and a.y_value != b.y_value
  # This removes duplicates
  and a.id < b.id
order by
  3 desc,
  1,
  2
;
