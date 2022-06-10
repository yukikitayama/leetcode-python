-- invoice
select
  a.invoice_id,
  b.customer_name,
  a.price,
  ifnull(c.contacts_cnt, 0) as contacts_cnt,
  ifnull(d.trusted_contacts_cnt, 0) as trusted_contacts_cnt
from
  invoices as a
left join
  customers as b
on
  a.user_id = b.customer_id

left join (
-- contacts_cnt
select
  user_id,
  count(*) as contacts_cnt
from
  contacts
group by
  user_id
) as c
on
  a.user_id = c.user_id

left join (
-- trusted_contacts_cnt
select
  user_id,
  count(*) as trusted_contacts_cnt
from
  contacts
where
  contact_name in (
    select
      customer_name
    from
      customers
  )
group by
  user_id
) as d
on
  a.user_id = d.user_id

order by
  a.invoice_id

;
