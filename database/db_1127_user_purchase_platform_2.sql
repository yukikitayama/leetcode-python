with
-- Compute total amount by spend_date, user and platform
cte1 as (
  select
    spend_date,
    user_id,
    sum(case when platform = 'mobile' then amount else 0 end) as mobile_amount,
    sum(case when platform = 'desktop' then amount else 0 end) as desktop_amount
  from
    spending
  group by
    1,
    2
),
-- Convert the above table into vertical form
cte2 as (
  select
    spend_date,
    user_id,
    if(mobile_amount >0, if(desktop_amount > 0, 'both', 'mobile'), 'desktop') as platform,
    mobile_amount + desktop_amount as amount
  from
    cte1
),
-- Aggregate the above
cte3 as (
  select
    spend_date,
    platform,
    sum(amount) as total_amount,
    count(distinct user_id) as  total_users
  from
    cte2
  group by
    1,
    2
),
-- Make all the combination of spend date and platform
cte4 as (
  select
    distinct spend_date,
    'mobile' as platform
  from
    spending
  union all
  select
    distinct spend_date,
    'desktop' as platform
  from
    spending
  union all
  select
    distinct spend_date,
    'both' as platform
  from
    spending
)

-- select * from cte1;
-- select * from cte2;
-- select * from cte3;
-- select * from cte4;

select
  a.spend_date,
  a.platform,
  ifnull(b.total_amount, 0) as total_amount,
  ifnull(b.total_users, 0) as total_users
from
  cte4 as a
left join
  cte3 as b
on
  a.spend_date = b.spend_date
  and a.platform = b.platform
;
