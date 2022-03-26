-- When multiple same employee IDs, use department_id with primary_flag is Y
-- When single employee ID, use the single department_id
-- Sort table by employee id, descending primary_flag, and use the first row for each employee id


SELECT
  employee_id,
  department_id
FROM
  Employee
WHERE
  primary_flag = 'Y'

UNION

SELECT
  employee_id,
  department_id
FROM
  employee
GROUP BY
  employee_id
HAVING
  COUNT(employee_id) = 1