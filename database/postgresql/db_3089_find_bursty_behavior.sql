-- Write your PostgreSQL query statement below

-- Get 2024 february data
with cte as (
  select
    *
  from
    posts
  where
    post_date between '2024-02-01' and '2024-02-28'
),

-- Compute average weekly posting frequency for each user
cte2 as (
  select
    user_id,
    count(post_id)::decimal / 4 as avg_weekly_posts
  from
    cte
  group by
    1
),

-- Compute how many posts were made in 7 window for each date
cte3 as (
  select
    user_id,
    post_date,
    count(*) over(
      partition by user_id
      -- 6 without single quotation doesn't work in PostgreSQL
      order by post_date range between interval '6' day preceding and current row
    ) as count_7window
  from
    cte
),

-- Compute max posting frequency in any 7 days windows to compare it with 2 * avg weekly post to get the at least any idea
cte4 as (
  select
    user_id,
    max(count_7window) as max_7day_posts
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
  b.max_7day_posts,
  a.avg_weekly_posts
from
  cte2 as a
join
  cte4 as b
on
  a.user_id = b.user_id
where
  b.max_7day_posts >= 2 * a.avg_weekly_posts
order by
  1
;
