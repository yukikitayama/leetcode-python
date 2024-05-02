-- Write your PostgreSQL query statement below
with cte as (
  select
    city,
    extract(hour from call_time) as calling_hour,
    count(caller_id) as number_of_calls,
    -- rank instead of row_number in case of a tie
    rank() over(
      partition by city
      order by count(caller_id) desc
    )
  from
    calls
  group by
    1,
    2
)

select
  city,
  calling_hour as peak_calling_hour,
  number_of_calls
from
  cte
where
  rank = 1
order by
  2 desc,
  1 desc
;
