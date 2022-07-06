select
  distinct a.user_id
from
  purchases as a
join
  purchases as b
on
  a.user_id = b.user_id
  and a.purchase_id != b.purchase_id
  and abs(datediff(a.purchase_date, b.purchase_date)) <= 7
order by
  1
;
