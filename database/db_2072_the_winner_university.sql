with cte1 as (
-- select
--   sum(if(score >= 90, 1, 0)) as num
-- from
--   newyork
select
  count(*) as num
from
  newyork
where
  score >= 90
),

cte2 as (
-- select
--   sum(if(score >= 90, 1, 0)) as num
-- from
--   california
select
  count(*) as num
from
  california
where
  score >= 90
)

select
  case
    when cte1.num > cte2.num then 'New York University'
    when cte1.num < cte2.num then 'California University'
    else 'No Winner'
  end as winner
from
  cte1,
  cte2

;