select
  sum(a.apple_count + ifnull(b.apple_count, 0)) as apple_count,
  sum(a.orange_count + ifnull(b.orange_count, 0)) as orange_count
from
  boxes as a
left join
  chests as b
on
  a.chest_id = b.chest_id
;
