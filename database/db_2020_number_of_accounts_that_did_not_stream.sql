select
  count(distinct account_id) as accounts_count
  -- distinct a.account_id
from
  subscriptions as a
where
  year(start_date) <= 2021
  and year(end_date) >= 2021
  and account_id not in (
    select
      account_id
    from
      streams
    where
      year(stream_date) = 2021
  )
;