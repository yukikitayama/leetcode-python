-- Write your PostgreSQL query statement below
select
  tweet_id
from
  tweets
where
  length(content) > 140
  or length(content) - length(replace(content, '@', '')) > 3
  or length(content) - length(replace(content, '#', '')) > 3
order by
  1