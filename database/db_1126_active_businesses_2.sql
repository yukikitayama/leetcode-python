with cte as (
select
  event_type,
  avg(occurences) as avg_activity
from
  events
group by
  1
)

select
  a.business_id
from
  events as a
left join
  cte as b
on
  a.event_type = b.event_type
where
  a.occurences > b.avg_activity
group by
  1
having
  count(a.event_type) > 1
;