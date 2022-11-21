-- account_id which had stream in 2021
# select
#   distinct account_id
# from
#   streams
# where
#   year(stream_date) = 2021
# ;

-- accounts that bought a subscription in 2021
# select
#   distinct account_id
# from
#   subscriptions
# where
#   year(start_date) <= 2021
#   and year(end_date) >= 2021
# ;

select
  count(distinct a.account_id) as accounts_count
from
  subscriptions as a
left join
  streams as b
on
  a.account_id = b.account_id
where
  year(a.start_date) <= 2021
  and year(a.end_date) >= 2021
  and a.account_id not in (
    select
      distinct account_id
    from
      streams
    where
      year(stream_date) = 2021
  )
;
