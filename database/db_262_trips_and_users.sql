# Write your MySQL query statement below
# select
#   a.request_at as Day,
#   round(sum(a.status != 'completed') / count(*), 2) as 'Cancellation Rate'
# from
#   trips as a
# join
#   users as b
# on
#   a.client_id = b.users_id
#   and b.banned = 'No'
# join
#   users as c
# on
#   a.driver_id = c.users_id
#   and c.banned = 'No'
# where
#   a.request_at between '2013-10-01' and '2013-10-03'
# group by
#   a.request_at
# ;


select
  a.request_at as Day,
  round(sum(a.status != 'completed') / count(*), 2) as 'Cancellation Rate'
from
  trips as a
where
  a.request_at between '2013-10-01' and '2013-10-03'
  and a.client_id in (select users_id from users where banned = 'No')
  and a.driver_id in (select users_id from users where banned = 'No')
group by
  a.request_at
;