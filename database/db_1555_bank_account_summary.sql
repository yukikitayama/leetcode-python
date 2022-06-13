-- Verions 1
select
  b.user_id,
  b.user_name,
  -- ifnull(_, 0) because some user could have no transaction, but left join gives us null
  b.credit + ifnull(c.amount, 0) as credit,
  if(b.credit + ifnull(c.amount, 0) < 0, 'Yes', 'No') as credit_limit_breached
from
  users as b
left join (
  -- Find amount delta as a whole by user_id
  select
    a.user_id,
    sum(a.amount) as amount
  from (
    -- Standardize amount +/- from transactions by user_id
    select
      paid_by as user_id,
      -1 * amount as amount
    from
      transactions
    union all
    select
      paid_to as user_id,
      amount as amount
    from
      transactions
  ) as a
  group by
    user_id
) as c
on
  b.user_id = c.user_id
;


-- Version 2
select
  user_id,
  user_name,
  ifnull(
    sum(
      case
        when a.user_id = b.paid_by then -amount
        else amount
      end
    ), 0) + a.credit as credit,
  case
    when ifnull(sum(
      case
        when a.user_id = b.paid_by then -amount
        else amount
      end
    ), 0) + a.credit >= 0 then 'No'
    else 'Yes'
  end as credit_limit_breached
from
  users as a
left join
  transactions as b
on
  a.user_id = b.paid_by
  or a.user_id = b.paid_to
group by
  a.user_id
;
