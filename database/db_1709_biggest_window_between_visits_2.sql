with
-- Assign numbers to know which rows are right after one date
cte1 as (
  select
    *,
    row_number() over(partition by user_id order by visit_date) as row_num
  from
    uservisits
),
-- Self-join to find the start date and end date to form a window
cte2 as (
  select
    a.user_id,
    a.visit_date as start_date,
    -- If there is not visit after the max date and before 2021-01-01, left join produces null in this column,
    -- so fill it with 2021-01-01 to make it possible to compute date difference later
    ifnull(b.visit_date, '2021-01-01') as end_date
  from
    cte1 as a
  left join
    cte1 as b
  on
    a.user_id = b.user_id
    -- Row number of end date will be equal to the row number of start date
    and a.row_num = b.row_num - 1
  where
    -- Just in case
    a.visit_date < '2021-01-01'
)

select
  user_id,
  -- datediff(later date, earlier date)
  max(datediff(end_date, start_date)) as biggest_window
from
  cte2
group by
  1
order by
  1
;