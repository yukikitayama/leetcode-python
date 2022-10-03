select
  concat(date_format(trans_date, "%Y"), "-", date_format(trans_date, "%m")) as month,
  country,
  count(state) as trans_count,
  sum(if(state = 'approved', 1, 0)) as approved_count,
  sum(amount) as trans_total_amount,
  sum(if(state = 'approved', amount, 0)) as approved_total_amount
from
  transactions
group by
  1,
  2
;