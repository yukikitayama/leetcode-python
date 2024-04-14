# Write your MySQL query statement below
with cte as (
  select
    turn,
    person_name,
    sum(weight) over(order by turn) as cumsum_weight
  from
    queue
)

select
  person_name
from
  queue
where
  turn = (
    select turn from cte where cumsum_weight <= 1000 order by cumsum_weight desc limit 1
  )
;
