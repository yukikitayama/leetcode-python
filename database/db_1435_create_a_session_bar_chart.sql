select
  b.bin,
  ifnull(count(s.session_id), 0) as total
from (
  select
    session_id,
    case
      when duration / 60 < 5 then '[0-5>'
      when duration / 60 >= 5 and duration / 60 < 10 then '[5-10>'
      when duration / 60 >= 10 and duration / 60 < 15 then '[10-15>'
      else '15 or more'
    end as bin
  from
    sessions
) as s
# To make a complete bin range
right join (
  select '[0-5>' as bin
  union all
  select '[5-10>' as bin
  union all
  select '[10-15>' as bin
  union all
  select '15 or more'
) as b
on
  s.bin = b.bin
group by
  b.bin
