select
  a.left_operand,
  a.operator,
  a.right_operand,
  case
    when a.operator = '>' and b.value > c.value then 'true'
    when a.operator = '<' and b.value < c.value then 'true'
    when a.operator = '=' and b.value = c.value then 'true'
    else 'false'
  end as value
from
  expressions as a
left join
  variables as b
on
  a.left_operand = b.name
left join
  variables as c
on
  a.right_operand = c.name
;
