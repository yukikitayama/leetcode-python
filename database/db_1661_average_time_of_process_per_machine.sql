select
  a.machine_id,
  round(
    sum(b.timestamp - a.timestamp) / count(distinct a.process_id),
    3
  ) as processing_time
from
  activity as a
left join
  activity as b
on
  a.machine_id = b.machine_id
  and a.process_id = b.process_id
  and a.timestamp < b.timestamp
where
  a.activity_type = 'start'
group by
  1
;
