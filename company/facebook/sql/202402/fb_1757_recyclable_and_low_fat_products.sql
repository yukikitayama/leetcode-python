-- Write your PostgreSQL query statement below
select
  product_id
from
  products
where
  -- PostgreSQL needs to use single quotes for string constants
  low_fats = 'Y'
  and recyclable = 'Y'
;