-- Write your PostgreSQL query statement below

/*
outer join keywords and posts
  on lower case word in lower content

group by post_id, concatenate topic_id by ", "
  if concatenate is null, 'Ambiguous!'
*/

with cte as (
  select
    distinct a.post_id,
    b.topic_id
  from
    posts as a
  left join
    keywords as b
  on
    -- Need to add spaces to allow word to match with a word in content, not a part of a word
    concat(' ', lower(a.content), ' ') like concat('% ', lower(b.word), ' %')
)

-- select * from cte;

select
  post_id,
  -- '10' < '2', but 2 < 10
  coalesce(string_agg(topic_id::text, ',' order by topic_id::numeric), 'Ambiguous!') as topic
from
  cte
group by
  post_id
;
