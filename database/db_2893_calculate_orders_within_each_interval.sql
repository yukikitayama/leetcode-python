# 1 - (1 - 1) % 6 = 1 - 0 % 6 = 1 - 0 = 1
# 6 - (6 - 1) % 6 = 6 - 5 % 6 = 6 - 5 = 1
# 7 - (7 - 1) % 6 = 7 - 6 % 6 = 7 - 0 = 7
# 8 - (8 - 1) % 6 = 8 - 7 % 6 = 8 - 1 = 7

with cte as (
  select
    *,
    -- Assign interval_no from order by group ID
    dense_rank() over(
      -- Assign group ID from minute column and 6 minutes rule
      order by minute - (minute - 1) % 6
    ) as interval_no
  from
    orders
)

select
  interval_no,
  sum(order_count) as total_orders
from
  cte
group by
  1
;