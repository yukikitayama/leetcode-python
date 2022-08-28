with cte as (
select
  salary,
  -- dense_rank() because if 2 100s and 1 50, we need to get 50, but if rank()
  -- rank of 50 will be 3.
  dense_rank() over(order by salary desc) as row_num
from
  employee
)

-- select * from cte;

select
  -- Use max() to allow us to return null if row_num = 2 doesn't exist
  max(salary) as SecondHighestSalary
from
  cte
where
  row_num = 2
;

with cte as (
select
  -- distinct because it could have a tie
  distinct salary as SecondHighestSalary
from
  employee
order by
  salary desc
limit
  1 offset 1
)

select max(SecondHighestSalary) as SecondHighestSalary from cte
;
