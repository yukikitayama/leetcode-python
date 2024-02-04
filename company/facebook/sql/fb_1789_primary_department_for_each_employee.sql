-- Write your PostgreSQL query statement below

-- Solution without group by having
-- with cte as (
--   select
--     employee_id,
--     count(distinct department_id) as dep_num
--   from
--     employee
--   group by
--     1
-- ),
-- cte2 as (
--   select
--     a.*,
--     b.dep_num
--   from
--     employee as a
--   left join
--     cte as b
--   on
--     a.employee_id = b.employee_id
-- )
-- select
--   employee_id,
--   department_id
-- from
--   cte2
-- where
--   dep_num = 1
-- union all
-- select
--   employee_id,
--   department_id
-- from
--   cte2
-- where
--   dep_num <> 1
--   and primary_flag = 'Y'
-- ;

-- Solution with group by having
with single_department as (
  select
    employee_id
  from
    employee
  group by
    employee_id
  having
    count(distinct department_id) = 1
)
select
  employee_id,
  department_id
from
  employee
where
  primary_flag = 'Y'
union all
select
  employee_id,
  department_id
from
  employee
where
  employee_id in (
    select employee_id from single_department
  )
  -- Some employee only has one row in employee and primary_flag is 'Y', but it should be 'N'
  and primary_flag = 'N'
;
