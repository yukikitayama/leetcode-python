with cte as (
select
  user_id,
  count(user_id) as contacts_cnt,
  count(b.email) as trusted_contacts_cnt
from
  contacts as a
left join
  customers as b
on
  a.contact_email = b.email
group by
  user_id
)

-- select * from cte;

select
  a.invoice_id,
  b.customer_name,
  a.price,
  ifnull(c.contacts_cnt, 0) as contacts_cnt,
  ifnull(c.trusted_contacts_cnt, 0) as trusted_contacts_cnt
from
  invoices as a
left join
  customers as b
on
  a.user_id = b.customer_id
left join
  cte as c
on
  a.user_id = c.user_id
order by
  1
;