# Write your MySQL query statement below
with cte as (
  select
    server_id,
    status_time as start_time,
    row_number() over(
      partition by server_id
      order by status_time
    ) as session_id
  from
    servers
  where
    session_status = 'start'
),

cte2 as (
  select
    server_id,
    status_time as end_time,
    row_number() over(
      partition by server_id
      order by status_time
    ) as session_id
  from
    servers
  where
    session_status = 'stop'
)

select
  floor(sum(timestampdiff(second, a.start_time, b.end_time) / 60 / 60) / 24) as total_uptime_days
from
  cte as a
left join
  cte2 as b
on
  a.server_id = b.server_id
  and a.session_id = b.session_id
;
