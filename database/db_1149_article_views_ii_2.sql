select
  distinct viewer_id as id
from
  views
group by
  viewer_id,
  view_date
having
  count(distinct article_id) > 1
order by
  viewer_id
;
