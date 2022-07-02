select
  a.first_col,
  b.second_col
from (
  select
    first_col,
    -- We need a column to merge
    row_number() over() as rn
  from
    data
  -- first_col in ascending order
  order by
    1
) as a
left join (
  select
    second_col,
    -- We need a column to merge
    row_number() over() as rn
  from
    data
  -- second_col in descending order
  order by
    1 desc
) as b
on
  a.rn = b.rn
;