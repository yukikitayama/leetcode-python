select
  a.member_id,
  a.name,
  # count(c.charged_amount) as num_purchase,
  # count(b.visit_id) as num_visit,
  # 100 * count(c.charged_amount) / count(b.visit_id) as conversion_rate,
  case
    when 100 * count(c.charged_amount) / count(b.visit_id) is null then 'Bronze'
    when 100 * count(c.charged_amount) / count(b.visit_id) >= 80 then 'Diamond'
    when 100 * count(c.charged_amount) / count(b.visit_id) >= 50 then 'Gold'
    else 'Silver'
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
  a.member_id,
  a.name
;