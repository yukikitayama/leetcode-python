with cte as (
  select
    lot_id,
    car_id,
    sum(fee_paid) as sum_fee,
    sum(timestampdiff(second, entry_time, exit_time) / 60 / 60) as sum_hour,
    rank() over(
      partition by car_id
      order by sum(timestampdiff(second, entry_time, exit_time) / 60 / 60) desc
    ) as rnk
  from
    parkingtransactions
  group by
    1,
    2
)

-- select * from cte;

select
  a.car_id,
  sum(a.sum_fee) as total_fee_paid,
  round(sum(a.sum_fee) / sum(a.sum_hour), 2) as avg_hourly_fee,
  b.lot_id as most_time_lot
from
  cte as a
inner join
  (select car_id, lot_id from cte where rnk = 1) as b
on
  a.car_id = b.car_id
group by
  1
order by
  1
;