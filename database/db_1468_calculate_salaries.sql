-- Version 1
select
  a.company_id,
  a.employee_id,
  a.employee_name,
  -- 1 - tax_rate because we wanna have remaining salary after tax
  round(a.salary * (1 - b.tax_rate), 0) as salary
from
  salaries as a
left join (
-- Tax rate by company
select
  company_id,
  case
    when max(salary) < 1000 then 0
    when max(salary) between 1000 and 10000 then 0.24
    else 0.49
  end as tax_rate
from
  salaries
group by
  company_id
) as b
on
  a.company_id = b.company_id

;

-- Version 2 with window function (Runtime is faster in LeetCode)
select
  company_id,
  employee_id,
  employee_name,
  round(
    case
      when max(salary) over(partition by company_id) < 1000 then salary
      when max(salary) over(partition by company_id) between 1000 and 10000 then salary * (1 - 0.24)
      else salary * (1 - 0.49)
    end,
    0
  ) as salary
from
  salaries
;
