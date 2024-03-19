-- Write your PostgreSQL query statement below
select
  round(sum(item_count * order_occurrences)::decimal / sum(order_occurrences), 2) as average_items_per_order
from
  orders