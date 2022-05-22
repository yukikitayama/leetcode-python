select
  transaction_id
from
  transactions
where
  (date(day), amount) in
  (
select
  date(day),
  max(amount) as max_amount
from
  transactions
group by
  date(day)
  )
order by
  transaction_id
;
