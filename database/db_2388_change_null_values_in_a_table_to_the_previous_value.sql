with
  cte1 as (
    select
      id,
      drink,
      row_number() over() as nb
    from
      coffeeshop
  ),
  cte2 as (
    select
      id,
      drink,
      nb,
      -- isnull() returns 1 if null and 0 if there's value
      sum(1 - isnull(drink)) over(order by nb) as group_id
    from
      cte1
  )

-- select * from cte1;
-- select * from cte2;

select
  id,
  first_value(drink) over(partition by group_id) as drink
from
  cte2
order by
  nb
;


