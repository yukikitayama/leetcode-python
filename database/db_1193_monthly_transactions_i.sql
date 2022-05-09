# Write your MySQL query statement below
select
  # if(month(trans_date) < 10,
  #   concat(year(trans_date), '-0', month(trans_date)),
  #   concat(year(trans_date), '-', month(trans_date))
  # ) as month,
  # left(trans_date, 7) as month,
  date_format(trans_date, '%Y-%m') as month,
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