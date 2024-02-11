-- Write your PostgreSQL query statement below

/*
cte
dense_rank()
  order by salary descending

select data where ranking = 2

edge
  one employee
    can return null
  two employee and they have the same salary
    will return null
  there are multple employees who has the same second highest salary
    return multiple people

if null

case when?
  if something then NULL
    something
      1. employee table has 1 employee
      2. multiple employees but they all has highest salary
  else secondhighestsalary

*/

with cte as (
  select
    *,
    dense_rank() over(
      order by salary desc
    ) as rnk
  from
    employee
)

select
  case
    when (select count(salary) from cte where rnk = 2) = 0 then null
    else (select distinct salary from cte where rnk = 2)
  end as SecondHighestSalary
;
