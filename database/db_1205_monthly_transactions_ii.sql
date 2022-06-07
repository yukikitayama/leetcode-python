select
  c.month,
  c.country,

  # sum(case when state = 'approved' then 1 else 0 end) as approved_count,
  # sum(case when state = 'approved' then c.amount else 0 end) as approved_amount,
  # sum(case when state = 'chargeback' then 1 else 0 end) as chargeback_count,
  # sum(case when state = 'chargeback' then c.amount else 0 end) as chargeback_amount

  sum(if(c.state = 'approved', 1, 0)) as approved_count,
  sum(if(c.state = 'approved', c.amount, 0)) as approved_amount,
  sum(if(c.state = 'chargeback', 1, 0)) as chargeback_count,
  sum(if(c.state = 'chargeback', c.amount, 0)) as chargeback_amount

from (
-- Create a table which contains both approve and chargeback records in
-- the same format
select
  date_format(a.trans_date, '%Y-%m') as month,
  b.country,
  'chargeback' as state,
  b.amount
from
  chargebacks as a
left join
  transactions as b
on
  a.trans_id = b.id

union all

select
  date_format(trans_date, '%Y-%m') as month,
  country,
  state,
  amount
from
  transactions
where
  state = 'approved'
) as c
group by
  1,
  2
;
