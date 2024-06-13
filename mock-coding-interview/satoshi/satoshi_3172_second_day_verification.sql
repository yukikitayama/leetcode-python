-- Write your PostgreSQL query statement below
select
  a.user_id
from
  emails as a
join
  texts as b
on
  a.email_id = b.email_id
where
  b.signup_action = 'Verified'
  and date_part('day', action_date::timestamp - signup_date::timestamp) = 1
order by
  1
;