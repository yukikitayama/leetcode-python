-- Find invoice_id which has the highest price by rank() of total price
-- also invoice_id should be the smallest
with cte as (
select
  a.invoice_id,
  rank() over(
      order by sum(a.quantity * b.price) desc, a.invoice_id
  ) as rnk
from
  purchases as a
left join
  products as b
on
  a.product_id = b.product_id
group by
  a.invoice_id
)

-- The details of the invoice needs to contain total price by each product
-- so left join to make the computation possible
select
  c.product_id,
  c.quantity,
  c.quantity * d.price as price
from
  purchases as c
left join
  products as d
on
  c.product_id = d.product_id
-- Filter invoice_id by subquery of using the CTE result
where
  invoice_id = (
    select invoice_id from cte where rnk = 1
  )
;
