-- Write your PostgreSQL query statement below
select
  a.name,
  b.bonus
from
  Employee as a
left join
  Bonus as b
on
  a.empId = b.empId
where
  b.bonus is null
  or b.bonus < 1000