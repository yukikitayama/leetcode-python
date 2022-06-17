select
  product_id,
  -- Use max because we are using group by, but not because we wanna get max
  -- we just want to show numbers
  max(case when store = 'store1' then price else null end) as store1,
  max(case when store = 'store2' then price else null end) as store2,
  max(case when store = 'store3' then price else null end) as store3
from
  products
group by
  1
;
