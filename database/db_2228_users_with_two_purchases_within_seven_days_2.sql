select
  distinct a.user_id
from
  purchases as a,
  purchases as b
where
  a.user_id = b.user_id
  and a.purchase_id != b.purchase_id
  and datediff(b.purchase_date, a.purchase_date) between 0 and 7
order by
  1
;
