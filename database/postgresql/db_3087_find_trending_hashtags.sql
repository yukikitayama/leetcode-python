select
  regexp_substr(tweet, '#[a-zA-Z]+') as hashtag,
  count(*) as hashtag_count
from
  tweets
where
  extract(year from tweet_date) = 2024
  and extract(month from tweet_date) = 2
group by
  1
order by
  2 desc,
  1 desc
limit
  3
;


