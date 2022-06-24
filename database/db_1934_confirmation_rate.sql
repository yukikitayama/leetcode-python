-- Version 1
# select
#   a.user_id,
#   ifnull(b.confirmation_rate, 0) as confirmation_rate
# from
#   signups as a
# left join (
# select
#   user_id,
#   round(sum(if(action = 'confirmed', 1, 0)) / count(action), 2) as confirmation_rate
# from
#   confirmations
# group by
#   user_id
# ) as b
# on
#   a.user_id = b.user_id

-- Verion 2
select
  a.user_id,
  round(avg(case
    when action = 'confirmed' then 1
    else 0
  end), 2) as confirmation_rate
from
  signups as a
left join
  confirmations as b
on
  -- Inflate
  a.user_id = b.user_id
group by
  1
;