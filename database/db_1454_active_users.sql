select
  distinct a.id,
  (select name from accounts where id = a.id) as name
from
  logins as a
join
  logins as b
on
  a.id = b.id
  -- b's login_date is first in datediff() because later date
  -- should be the first argument to take difference
  and datediff(b.login_date, a.login_date) between 1 and 4
group by
  a.id,
  a.login_date
having
  -- 4 because 1 <= diff <= 4 are joined, so date itself doesn't
  -- need to be included
  -- Add distinct because a user may login multiple times in
  -- the same day, so it would have 4 records, but these are the
  -- same day, but that's not what we want
  count(distinct b.login_date) = 4

;
