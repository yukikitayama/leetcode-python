with cte as (
  select
    a.seller_id,
    count(distinct a.item_id) as num_items
  from
    orders as a
  left join
    items as b
  on
    a.item_id = b.item_id
  left join
    users as c
  on
    a.seller_id = c.seller_id
  where
    -- Items need to be different from their favorite brand
    b.item_brand <> c.favorite_brand
  group by
    1
)

select
  seller_id,
  num_items
from
  cte
where
  -- Show only top sellers
  num_items = (
    select max(num_items) from cte
  )
order by
  1
;