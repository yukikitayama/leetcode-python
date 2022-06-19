# -- Total income by month
# select
#   account_id,
#   date_format(day, '%Y-%m') as month,
#   sum(case
#     when type = 'Creditor' then amount
#     else 0
#   end) as income
# from
#   transactions
# group by
#   1,
#   2

with cte as (
  select
    a.account_id,
    date_format(a.day, '%Y%m') as date,
    sum(a.amount) as income,
    b.max_income
  from
    transactions as a
  left join
    accounts as b
  on
    a.account_id = b.account_id
  where
    a.type = 'Creditor'
  group by
    a.account_id,
    date_format(a.day, '%Y%m')
  having
    -- Suspicious activity
    sum(a.amount) > b.max_income
)

-- select * from cte

-- Find two or more consecutive months
select
  c.account_id
from
  cte as c,
  cte as d
where
  c.account_id = d.account_id
  and period_diff(c.date, d.date) = 1
group by
  1
order by
  1

;