select
  a.pay_month,
  a.department_id,
  case
    when a.department_avg > b.company_avg then 'higher'
    when a.department_avg < b.company_avg then 'lower'
    else 'same'
  end as comparison
from (
select
  department_id,
  date_format(pay_date, '%Y-%m') as pay_month,
  avg(amount) as department_avg
from
  salary
join
  employee
on
  salary.employee_id = employee.employee_id
group by
  1,
  2
) as a
join (
select
  date_format(pay_date, '%Y-%m') as pay_month,
  avg(amount) as company_avg
from
  salary
group by
  1
) as b
on
  a.pay_month = b.pay_month
;
