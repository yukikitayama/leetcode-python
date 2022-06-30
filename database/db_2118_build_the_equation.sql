select
  concat(
    group_concat(
      a.term
      -- The powers in the LHS should be sorted in descending order
      order by a.power desc
      separator ''
    ),
    -- The RHS should be zero
    '=0'
  ) as equation
from (
select
  power,
  factor,
  concat(
    case
      when factor > 0 then '+'
      -- '' because we will use '-' in factor if negative
      else ''
    end,
    factor,
    case
      when power = 0 then ''
      else 'X'
    end,
    case
      when power = 0 or power = 1 then ''
      else '^'
    end,
    case
      when power = 0 or power = 1 then ''
      else power
    end
  ) as term
from
  terms
-- order by
--  power desc
) as a
;
