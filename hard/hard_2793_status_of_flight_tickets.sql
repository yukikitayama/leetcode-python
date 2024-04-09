/*
Join flight capacity to passengers table
Assing row number order by booking time within flight ID
If row number is <= capacity, confirmed, otherwise waitlist
*/

# Write your MySQL query statement below

with cte as (
  select
    a.passenger_id,
    row_number() over(
      partition by a.flight_id
      order by a.booking_time
    ) as row_num,
    b.capacity
  from
    passengers as a
  left join
    flights as b
  on
    a.flight_id = b.flight_id
)

select
  passenger_id,
  if(row_num <= capacity, "Confirmed", "Waitlist") as Status
from
  cte
order by
  1
;
