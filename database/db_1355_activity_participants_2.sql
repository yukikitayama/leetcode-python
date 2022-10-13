-- Find the number of participants in each activity
with cte as (
  select
    activity,
    count(*) as num_participants
  from
    friends
  group by
    1
)

select
  activity
from
  friends
group by
  1
having
  -- neither the maximum
  count(*) != (
    select max(num_participants) from cte
  )
  -- nor the minimum
  and count(*) != (
    select min(num_participants) from cte
  )
;