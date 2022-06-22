-- The result table must contain all the categories,
-- so we create the categories in advance
with cte as (
select
  'Low Salary' as category
union all
select
  'Average Salary' as category
union all
select
  'High Salary' as category
)

select
  a.category,
  -- left join gives us null if nothing joined, so convert null to 0
  -- for the problem requirement
  ifnull(b.accounts_count, 0) as accounts_count
from
  cte as a
left join (
-- Compute salary categories
select
  case
    when income < 20000 then 'Low Salary'
    when income > 50000 then 'High Salary'
    else 'Average Salary'
  end as category,
  count(*) as accounts_count
from
  accounts
group by
  1
) as b
on
  a.category = b.category

;