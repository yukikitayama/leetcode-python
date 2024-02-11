# Write your MySQL query statement below

/*
Self-join by machine id and process id
average of end t - start t by machine id
*/

with
start as (
  select
    machine_id,
    process_id,
    timestamp as start
  from
    activity
  where
    activity_type = 'start'
),

end as (
  select
    machine_id,
    process_id,
    timestamp as end
  from
    activity
  where
    activity_type = 'end'
)

select
  a.machine_id,
  round(avg(b.end - a.start), 3) as processing_time
from
  start as a
left join
  end as b
on
  a.machine_id = b.machine_id
  and a.process_id = b.process_id
group by
  1
;

-- select
--   machine_id,
--   round(
--     sum(
--       case
--         when activity_type = 'start' then -timestamp
--         else timestamp
--       end
--     ) / (select count(distinct process_id)),
--     3
--   ) as processing_time
-- from
--   activity
-- group by
--   machine_id
-- ;
