CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

  # RETURN (
  #     # Write your MySQL query statement below.

#       with cte as (
#         select
#           salary,
#           dense_rank() over(order by salary desc) as rnk
#         from
#           employee
#       )

#       select
#         max(salary)
#       from
#         cte
#       where
#         rnk = N
#  );

  declare m int;
  set m = n - 1;
  return (
      select
        distinct salary
      from
        employee
      order by
        salary desc
      limit
        1 offset m
  );
END