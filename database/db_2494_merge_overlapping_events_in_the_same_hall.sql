with
cte1 as (
  select
    *,
    -- ifnull because the first event in each hall_id doesn't have the preceding end_day,
    -- so max() over() returns null, and start_day > max() over() returns null,
    -- but it's still the enw starting event, so assign 1
    ifnull(
      -- This comparison gives us 1 or 0
      start_day > max(end_day) over(
        partition by hall_id
        order by start_day, end_day desc
        -- unbounded preceding checks all rows before the current row
        -- 1 preceding checks 1 row before the current row
        rows between unbounded preceding and 1 preceding
      )
    , 1) as is_new_event_start
  from
    hallevents
),
cte2 as (
  select
    hall_id,
    start_day,
    end_day,
    -- Assign the same event_id to events which are overlaped
    sum(is_new_event_start) over(
      partition by hall_id
      order by start_day, end_day desc
    ) as event_id
  from
    cte1
)

-- select * from cte1;
-- select * from cte2;

select
  hall_id,
  -- Aggregate multiple events with the same event_id by the fast day and last day among the events
  min(start_day) as start_day,
  max(end_day) as end_day
from
  cte2
group by
  hall_id,
  event_id
;
