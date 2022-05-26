select
  b.stats as period_state,
  min(b.day) as start_date,
  max(b.day) as end_date
from (

select
  day,
  rank() over(order by day) as overall_ranking,
  stats,
  rk,
  -- inv gives us the group to aggregate conriguous days with the same stats
  rank() over(order by day) - rk as inv
from (

select
  fail_date as day,
  'failed' as stats,
  rank() over(order by fail_date) as rk
from
  failed
where
  fail_date between '2019-01-01' and '2019-12-31'

union

select
  success_date as day,
  'succeeded' as stats,
  rank() over(order by success_date) as rk
from
  succeeded
where
  success_date between '2019-01-01' and '2019-12-31'

) as a


) as b

group by
  inv, stats
order by
  2

;
