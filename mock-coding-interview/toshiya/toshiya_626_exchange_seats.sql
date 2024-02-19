-- Write your PostgreSQL query statement below

select
  a.id,
  case
    when (select max(id) from seat) % 2 = 1 and a.id = (select max(id) from seat) then a.student
    -- id starts from 1, not 0
    when a.id % 2 = 1 then b.student
    when a.id % 2 = 0 then c.student
  end as student
from
  seat as a
left join
  seat as b
on
  a.id + 1 = b.id
left join
  seat as c
on
  a.id - 1 = c.id
;

-- select
--   case
--     when id % 2 = 1 and id <> (select max(id) from seat) then id + 1
--     when id % 2 = 1 and id = (select max(id) from seat) then id
--     else id - 1
--   end as id,
--   student
-- from
--   seat
-- order by
--   1
-- ;
