-- Write your PostgreSQL query statement below
with cte as (
  select
    extract(week from a.purchase_date) - extract(week from '2023-11-01'::timestamp) + 1 as week_of_month,
    b.membership,
    sum(a.amount_spend) as total_amount
  from
    purchases as a
  left join
    users as b
  on
    a.user_id = b.user_id
  where
    -- Sunday: 0, Saturday: 6
    extract(dow from a.purchase_date) = 5
    and b.membership in ('Premium', 'VIP')
  group by
    1,
    2
),

cte2 as (
  select 1 as week_of_month, 'Premium' as membership
  union
  select 1 as week_of_month, 'VIP' as membership
  union
  select 2 as week_of_month, 'Premium' as membership
  union
  select 2 as week_of_month, 'VIP' as membership
  union
  select 3 as week_of_month, 'Premium' as membership
  union
  select 3 as week_of_month, 'VIP' as membership
  union
  select 4 as week_of_month, 'Premium' as membership
  union
  select 4 as week_of_month, 'VIP' as membership
)

select
  a.*,
  coalesce(b.total_amount, 0) as total_amount
from
  cte2 as a
left join
  cte as b
on
  a.week_of_month = b.week_of_month
  and a.membership = b.membership
order by
  1,
  2
;