with
cte1 as (
  select
    id,
    drink,
    row_number() over() as row_num
  from
    coffeeshop
),
cte2 as (
  select
    id,
    drink,
    row_num,
    -- sum(col1) over() gives us the cumulative sum of col1
    -- when null, 0 is added to the cumulative sum
    -- so the non-null and the subsequent null have the same values
    sum(1 - isnull(drink)) over(order by row_num) as group_id
  from
    cte1
)

-- select * from cte1
-- select * from cte2

select
  id,
  first_value(drink) over(partition by group_id order by row_num) as drink
from
  cte2
;