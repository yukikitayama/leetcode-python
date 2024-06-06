-- Write your PostgreSQL query statement below
with cte as (
  select
    num,
    count(*) as count
  from
    mynumbers
  group by
    1
)

select
  max(num) as num
from
  mynumbers
where
  num not in (
    select num from cte where count > 1
  )
;