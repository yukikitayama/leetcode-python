/*
Since some fridays might be missing, so manually create output table purchase_date column
Group by sum amount_spend from purchases table filter dayofweek is 6
The manula table as base table of left join and join group by sum table
  if null, replace with 0
*/

# Write your MySQL query statement below
with cte as (
  select 1 as week_of_month, date '2023-11-03' as purchase_date
  union
  select 2 as week_of_month, date '2023-11-10' as purchase_date
  union
  select 3 as week_of_month, date '2023-11-17' as purchase_date
  union
  select 4 as week_of_month, date '2023-11-24' as purchase_date
),

cte2 as (
  select
    purchase_date,
    sum(amount_spend) as total_amount
  from
    purchases
  where
    dayofweek(purchase_date) = 6
  group by
    1
)

select
  a.week_of_month,
  a.purchase_date,
  ifnull(b.total_amount, 0) as total_amount
from
  cte as a
left join
  cte2 as b
on
  a.purchase_date = b.purchase_date
;
