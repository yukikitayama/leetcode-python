select
  a.reports_to as employee_id,
  b.name,
  count(a.age) as reports_count,
  round(avg(a.age), 0) as average_age
from
  employees as a
left join
  employees as b
on
  a.reports_to = b.employee_id
where
  a.reports_to is not null
group by
  a.reports_to
order by
  1
;