# Write your MySQL query statement below
with cte as (
  select
    user_id,
    count(distinct loan_type) as c
  from
    loans
  where
    loan_type = 'Refinance'
    or loan_type = 'Mortgage'
  group by
    1
)

select
  distinct user_id
from
  cte
where
  c = 2
order by
  1
;