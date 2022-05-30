select
  distinct a.*
from
  -- Join all tables horizontally
  stadium as a,
  stadium as b,
  stadium as c
where
  -- People in each date needs to be greater than or equal to 100
  a.people >= 100
  and b.people >= 100
  and c.people >= 100
  -- Id needs to be consecutive 3 times or more
  and (
    -- a, b, c
    (a.id - b.id = 1 and a.id - c.id = 2 and b.id - c.id = 1)
    -- b, a, c
    or (b.id - a.id = 1 and b.id - c.id = 2 and a.id - c.id = 1)
    -- c, b, a
    or (c.id - b.id = 1 and b.id - a.id = 1 and c.id - a.id = 2)
  )
-- Remove duplicates
order by
  a.id
;
