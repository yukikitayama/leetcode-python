select
  a.employee_id,
  b.team_size
from
  employee as a
left join
  (
select
  team_id,
  count(*) as team_size
from
  employee
group by
  team_id
  ) as b
on
  a.team_id = b.team_id
;