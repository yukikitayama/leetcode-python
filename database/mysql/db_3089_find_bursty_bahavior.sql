# Write your MySQL query statement below

with cte as (
  select
    *
  from
    posts
  where
    post_date between '2024-02-01' and '2024-02-28'
),

cte2 as (
  select
    user_id,
    count(*) / 4 as avg_weekly_posts
  from
    cte
  group by
    1
),

cte3 as (
  select
    user_id,
    post_date,
    count(*) over(
      partition by user_id
      order by post_date range between interval 6 day preceding and current row
    ) as cnt7
  from
    cte
),

cte4 as (
  select
    user_id,
    max(cnt7) as max_7day_posts
  from
    cte3
  group by
    1
)

-- select * from cte;
-- select * from cte2;
-- select * from cte3;
-- select * from cte4;

select
  a.user_id,
  a.max_7day_posts,
  b.avg_weekly_posts
from
  cte4 as a
join
  cte2 as b
on
  a.user_id = b.user_id
where
  b.avg_weekly_posts * 2 <= max_7day_posts
order by
  1
;