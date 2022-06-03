# Write your MySQL query statement below
select
  distinct viewer_id as id
  # view_date,
  # count(distinct article_id) as num_article
from
  views
group by
  viewer_id,
  view_date
having
  count(distinct article_id) > 1
order by
  1
;
