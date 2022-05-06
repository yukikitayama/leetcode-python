select
  a.name,
  ifnull(sum(b.distance), 0) as travelled_distance
from
  users as a
left join
  rides as b
on
  a.id = b.user_id
group by
  a.name
order by
  2 desc,
  1
;