with
cte1 as (
  select
    date_format(pay_date, '%Y-%m') as pay_month,
    avg(amount) as company_salary
  from
    salary
  group by
    1
),
cte2 as (
  select
    date_format(pay_date, '%Y-%m') as pay_month,
    b.department_id,
    avg(a.amount) as department_salary
  from
    salary as a
  left join
    employee as b
  on
    a.employee_id = b.employee_id
  group by
    1,
    2
)

-- select * from cte1;
-- select * from cte2;

select
  a.pay_month,
  a.department_id,
  case
    when a.department_salary > b.company_salary then 'higher'
    when a.department_salary < b.company_salary then 'lower'
    else 'same'
  end as comparison
from
  cte2 as a
left join
  cte1 as b
on
  a.pay_month = b.pay_month
;