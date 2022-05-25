-- Group by year, datediff

select
  a.product_id,
  b.product_name,
  a.report_year,
  a.total_amount

from (

select
  product_id,
  '2018' as report_year,
  -- +1 to make both start and end inclusive
  average_daily_sales * (datediff(
    least(period_end, '2018-12-31'),
    greatest(period_start, '2018-01-01')
  ) + 1) as total_amount
from
  sales
where
  -- OR because period may pass multiple years
  year(period_start) = 2018
  or year(period_end) = 2018

union

select
  product_id,
  '2019' as report_year,
  -- +1 to make both start and end inclusive
  average_daily_sales * (datediff(
    least(period_end, '2019-12-31'),
    greatest(period_start, '2019-01-01')
  ) + 1) as total_amount
from
  sales
where
  -- AND because both start and end need to pass 2019
  year(period_start) <= 2019
  and year(period_end) >= 2019

union

select
  product_id,
  '2020' as report_year,
  -- +1 to make both start and end inclusive
  average_daily_sales * (datediff(
    least(period_end, '2020-12-31'),
    greatest(period_start, '2020-01-01')
  ) + 1) as total_amount
from
  sales
where
  -- OR because period may pass multiple years
  year(period_start) = 2020
  or year(period_end) = 2020

) as a

left join
  product as b
on
  a.product_id = b.product_id
order by
  a.product_id,
  a.report_year
;
