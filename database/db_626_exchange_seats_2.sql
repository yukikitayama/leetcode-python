select
  case
    -- Even
    when mod(id, 2) = 0 then id - 1
    -- Odd but last person
    when mod(id, 2) != 0 and id = num then id
    -- Odd
    else id + 1
  end as id,
  student
from
  seat,
  (select count(*) as num from seat) as a
order by
  1
;