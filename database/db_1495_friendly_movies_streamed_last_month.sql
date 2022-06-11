select
  distinct b.title
from
  tvprogram as a
left join
  content as b
on
  a.content_id = b.content_id
where
  b.kids_content = 'Y'
  and b.content_type = 'Movies'
  and year(a.program_date) = 2020
  and month(a.program_date) = 6
;
