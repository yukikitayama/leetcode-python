with recursive
cte as (
  select
    min(period_start) as date
  from
    sales
  union all
  select
    date_add(date, interval 1 day) as date
  from
    cte
  where
    date < (
      select max(period_end) from sales
    )
)

-- select * from cte1;

select
  b.product_id,
  c.product_name,
  -- YEAR(a.date) only didn't work
  cast(year(a.date) as char) as report_year,
  sum(b.average_daily_sales) as total_amount
from
  cte as a
inner join
  sales as b
on
  a.date >= b.period_start
  and a.date <= b.period_end
inner join
  product as c
on
  b.product_id = c.product_id
group by
  1,
  2,
  3
order by
  1,
  3
;
