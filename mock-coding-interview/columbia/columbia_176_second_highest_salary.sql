-- Write your PostgreSQL query statement below
with cte as (
  select
    *,
    dense_rank() over(order by salary desc) as rnk
  from
    employee
)

select
  case
    when (select distinct salary from cte where rnk = 2) is null then null
    else (select distinct salary from cte where rnk = 2)
  end as SecondHighestSalary
;

# Write your MySQL query statement below
-- with cte as (
--   select
--     *
--   from
--     employee
--   union all
--   select
--     -1,
--     null
-- ),

-- cte2 as (
--   select
--     *,
--     dense_rank() over(order by salary desc) as rnk
--   from
--     cte
-- )

-- -- select * from cte2

-- select
--   distinct salary as SecondHighestSalary
-- from
--   cte2
-- where
--   rnk = 2
-- ;

with cte as (
  select
    *,
    dense_rank() over(order by salary desc) as rnk
  from
    employee
)

select
  ifnull(
    (select distinct salary from cte where rnk = 2),
    null
  ) as SecondHighestSalary
