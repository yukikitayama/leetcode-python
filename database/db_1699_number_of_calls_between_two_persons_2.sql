with cte as (
  select
    from_id,
    to_id,
    duration
  from
    calls
  where
    from_id < to_id
  union all
  select
    to_id as from_id,
    from_id as to_id,
    duration
  from
    calls
  where
    to_id < from_id
)

-- select * from cte;

select
  from_id as person1,
  to_id as person2,
  count(*) as call_count,
  sum(duration) as total_duration
from
  cte
group by
  1,
  2
;