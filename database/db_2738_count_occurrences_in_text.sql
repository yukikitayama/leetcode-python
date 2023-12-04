select
  'bull' as word,
  count(*) as count
from
  files
where
  content like '% bull %'

union

select
  'bear' as word,
  count(*) as count
from
  files
where
  content like '% bear %'
;
