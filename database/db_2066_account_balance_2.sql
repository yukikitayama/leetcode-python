select
  account_id,
  day,
  sum(
    case
      when type = 'Deposit' then amount
      else -amount
    end
  ) over (partition by account_id order by day) as balance
from
  transactions
group by
  1,
  2
;
