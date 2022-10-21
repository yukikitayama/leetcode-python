select
  distinct a.id,
  (select name from accounts where id = a.id) as name
from
  logins as a
join
  logins as b
on
  a.id = b.id
  and datediff(b.login_date, a.login_date) between 1 and 4
group by
  a.id,
  -- a.login_date as early days of consecutive days
  a.login_date
having
  -- b.login_date as last day of consecutive day
  count(distinct b.login_date) = 4
;
