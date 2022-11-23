select
  a.member_id,
  a.name,
  case
    when count(c.visit_id) / count(b.visit_id) >= 0.8 then 'Diamond'
    when count(c.visit_id) / count(b.visit_id) >= 0.5 then 'Gold'
    when count(c.visit_id) / count(b.visit_id) < 0.5 then 'Silver'
    else 'Bronze'
  end as category
from
  members as a
left join
  visits as b
on
  a.member_id = b.member_id
left join
  purchases as c
on
  b.visit_id = c.visit_id
group by
  1,
  2
;