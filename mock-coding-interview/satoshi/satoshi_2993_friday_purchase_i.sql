# Write your MySQL query statement below
select
  week(purchase_date) - week('2023-11-01') + 1 as week_of_month,
  purchase_date,
  sum(amount_spend) as total_amount
from
  purchases
where
  -- 1: Sunday, 7: Saturday
  dayofweek(purchase_date) = 6
  and year(purchase_date) = 2023
  and month(purchase_date) = 11
group by
  1,
  2
order by
  1
;
