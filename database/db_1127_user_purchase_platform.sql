select
  b.spend_date,
  b.platform,
  ifnull(sum(c.amount), 0) as total_amount,
  count(c.user_id) as total_users
from
(
select
  distinct(spend_date) as spend_date,
  'desktop' as platform
from
  spending
union
select
  distinct(spend_date) as spend_date,
  'mobile' as platform
from
  spending
union
select
  distinct(spend_date) as spend_date,
  'both' as platform
from
  spending
) as b
left join (
select
  spend_date,
  user_id,
  if(mobile_amount > 0, if(desktop_amount > 0, 'both', 'mobile'), 'desktop') as platform,
  mobile_amount + desktop_amount as amount
from (
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
) as a
) as c
on
  b.spend_date = c.spend_date
  and b.platform = c.platform
group by
  spend_date,
  platform



;
