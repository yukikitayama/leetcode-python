select
  bike_number,
  max(end_time) as end_time
from
  bikes
group by
  1
order by
  2 desc
;
