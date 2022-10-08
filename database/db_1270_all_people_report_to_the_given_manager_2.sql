
# with
# cte1 as (
#   -- Direct reporting to the head
#   select
#     employee_id
#   from
#     employees
#   where
#     manager_id = 1
#     and employee_id != 1
# ),

# -- Indirect reporting to the head with 1 manager
# cte2 as (
#   select
#     employee_id
#   from
#     employees
#   where
#     manager_id in (
#       select * from cte1
#     )
# ),

# -- Indirect reporting to the head with 2 managers
# cte3 as (
#   select
#     employee_id
#   from
#     employees
#   where
#     manager_id in (
#       select * from cte2
#     )
# )

# select
#   *
# from
#   cte1
# union
# select
#   *
# from
#   cte2
# union
# select
#   *
# from
#   cte3
# ;

select
  a.employee_id
from
  employees as a
left join
  employees as b
on
  a.manager_id = b.employee_id
left join
  employees as c
on
  b.manager_id = c.employee_id
where
  a.employee_id != 1
  and c.manager_id = 1
;
