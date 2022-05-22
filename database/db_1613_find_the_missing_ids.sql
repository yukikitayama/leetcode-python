-- I need to generate numbers
# Write your MySQL query statement below
with recursive cte as
(
  select 1 as id_candidate
  union all
  select id_candidate + 1
  from cte
  where id_candidate <
  (
    select max(customer_id)
    from customers
  )
)

select id_candidate as ids
from cte
where id_candidate not in
(
  select customer_id
  from customers
)
