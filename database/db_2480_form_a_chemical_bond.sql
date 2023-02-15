select
  a.symbol as metal,
  b.symbol as nonmetal
from
  elements as a,
  elements as b
where
  a.type = "Metal"
  and b.type = "Nonmetal"
;
