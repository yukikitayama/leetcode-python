with cte as (
  select
    *,
    sum(frequency) over(order by num) as cumulative_freq,
    -- Add over() to put the sums to all the rows, not aggregating
    (sum(frequency) over()) / 2 as median_freq
  from
    numbers
)

-- select * from cte;

select
  avg(num) as median
from
  cte
where
  -- cumulative_freq - frequency is lower bound
  -- cumulative_freq is upper bound
  median_freq between cumulative_freq - frequency and cumulative_freq
;
