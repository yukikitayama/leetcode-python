/*
Extract words starting with #
*/


# Write your MySQL query statement below
with recursive cte as (
  select
    *
  from
    tweets
  where
    year(tweet_date) = 2024
    and month(tweet_date) = 2
),

cte2 as (
  select
    regexp_substr(tweet, '#[a-zA-Z]+') as hashtag,
    regexp_replace(tweet, '#[a-zA-Z]+', '', 1, 1) as tweet
  from
    cte
  union all
  select
    regexp_substr(tweet, '#[a-zA-Z]+') as hashtag,
    regexp_replace(tweet, '#[a-zA-Z]+', '', 1, 1) as tweet
  from
    cte2
  -- In recursion, eventually we finish searching all the tags, and regexp_substr() returns null
  where
    hashtag is not null
)

select
  hashtag,
  count(*) as count
from
  cte2
where
  hashtag is not null
group by
  1
order by
  2 desc,
  1 desc
limit
  3
;
