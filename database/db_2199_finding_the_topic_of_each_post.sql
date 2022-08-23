select
  p.post_id,
  -- distinct because should not contain duplicate IDs
  -- order by because topic IDs should be ordered ascending
  -- ifnull because left join produces null if no topic_id are joined, but
  -- the problem requires to return ambiguous if a post does not have keywords
  ifnull(group_concat(distinct k.topic_id order by k.topic_id), 'Ambiguous!') as topic
from
  posts as p
left join
  keywords as k
on
  -- spaces for '% ' and ' %' are due to start and end of a word existing in p.content
  concat(' ', lower(p.content), ' ') like concat('% ', lower(k.word), ' %')
group by
  1
;
