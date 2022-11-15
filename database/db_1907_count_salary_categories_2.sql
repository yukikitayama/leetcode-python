with
-- Create category table to report 0 for no accounts in a category
cte1 as (
  select
    'Low Salary' as category
  union
  select
    'Average Salary' as category
  union
  select
    'High Salary' as category
),
-- Create category column to count
cte2 as (
  select
    *,
    case
      when income < 20000 then 'Low Salary'
      when income > 50000 then 'High Salary'
      else 'Average Salary'
    end as category
  from
    accounts
),
-- Count accounts by category
cte3 as (
  select
    category,
    count(*) as accounts_count
  from
    cte2
  group by
    1
)

select
  a.category,
  -- If there are no accounts in a category, report 0
  ifnull(b.accounts_count, 0) as accounts_count
from
  cte1 as a
left join
  cte3 as b
on
  a.category = b.category
;