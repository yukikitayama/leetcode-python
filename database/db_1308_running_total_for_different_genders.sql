select
  # a is the base
  a.gender,
  a.day,
  # b is the data connected by b day <= a day
  # so we sum b to accumulate
  sum(b.score_points) as total
from
  scores as a,
  scores as b
where
  a.gender = b.gender
  and b.day <= a.day
group by
  a.gender,
  a.day
order by
  a.gender,
  a.day
;
