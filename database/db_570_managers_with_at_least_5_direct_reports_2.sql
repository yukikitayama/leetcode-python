-- managerId with at least 5 direct reports
with cte as (
select
  managerId
from
  employee
group by
  managerId
having
  count(*) >= 5
)

select
  a.name
from
  employee as a
inner join
  cte as b
on
  a.id = b.managerId
;