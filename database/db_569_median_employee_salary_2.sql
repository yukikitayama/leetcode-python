with cte as (
select
  *,
  row_number() over(partition by company order by salary, id) as row_num,
  row_number() over(partition by company order by salary desc, id desc) as rev_row_num
from
  employee
)

select
  id,
  company, salary
from
  cte
where
  rev_row_num between row_num - 1 and row_num + 1
;
