with cte as (
  select
    visited_on,
    sum(amount) as day_sum
  from
    customer
  group by
    1
)

select
  a.visited_on,
  sum(b.day_sum) as amount,
  round(avg(b.day_sum), 2) as average_amount
from
  -- Merge horizontally
  cte as a,
  cte as b
where
  datediff(a.visited_on, b.visited_on) between 0 and 6
group by
  a.visited_on
having
  count(a.visited_on) = 7
;