"""
{"headers": {
"Employee": ["Id", "Name", "Salary", "DepartmentId"],
"Department": ["Id", "Name"]
},
"rows": {"Employee": [
[1, "Joe", 85000, 1],
[2, "Henry", 80000, 2],
[3, "Sam", 60000, 2],
[4, "Max", 90000, 1],
[5, "Janet", 69000, 1],
[6, "Randy", 85000, 1],
[7, "Will", 70000, 1]
],
"Department": [
[1, "IT"],
[2, "Sales"]
]}}
"""


# Write your MySQL query statement below
# select
#   e1.Name as 'Employee',
#   e1.Salary
# from
#   Employee e1

# select
#   count(distinct e2.Salary)
# from
#   Employee e2

# select
#   e1.Name as 'Employee',
#   e1.Salary
# from
#   Employee e1
# where 3 > (
#   select count(distinct e2.Salary)
#   from Employee e2
#   where e2.Salary > e1.Salary
# )

# select count(distinct e2.Salary)
# from Employee e2, Employee e1
# where e2.Salary > e1.Salary


select
    d.Name as 'Department',
    e1.Name as 'Employee',
    e1.Salary
from
    Employee e1
join
    Department d
on
    e1.DepartmentId = d.Id
where
    3 > (
        select
            count(distinct e2.Salary)
        from
            Employee e2
        where
            e2.Salary > e1.Salary
            and e1.DepartmentId = e2.DepartmentId
    )
;
