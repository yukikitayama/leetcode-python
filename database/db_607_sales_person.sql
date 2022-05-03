select
  c.name
from
  salesperson as c
where
  c.sales_id not in (
    select
      a.sales_id
    from
      orders as a
    left join
      company as b
    on
      a.com_id = b.com_id
    where
      b.name = 'RED'
  )
;