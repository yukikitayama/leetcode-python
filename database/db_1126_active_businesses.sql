select
  b.business_id
from

(
select
  event_type,
  avg(occurences) as avg_occurences
from
  events
group by
  event_type
) as a

join
  events as b
on
  a.event_type = b.event_type
where
  b.occurences > a.avg_occurences
group by
  b.business_id
having
  count(distinct b.event_type) > 1

;
