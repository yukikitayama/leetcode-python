delete
  a
from
  person as a,
  person as b
where
  a.email = b.email
  and a.id > b.id
;