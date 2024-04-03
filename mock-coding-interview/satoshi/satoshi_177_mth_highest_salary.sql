-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--     # Declare
--    declare m int;
--    set m = N - 1;

--   RETURN (
--       # Write your MySQL query statement below.
--     with cte as (
--         select
--           salary,
--           dense_rank() over(order by salary desc) as rnk
--         from
--           employee
--     )

--     select distinct salary from cte where rnk = m + 1
--   );
-- END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

  RETURN (
      # Write your MySQL query statement below.
    with cte as (
        select
          salary,
          dense_rank() over(order by salary desc) as rnk
        from
          employee
    )

    select distinct salary from cte where rnk = n
  );
END