-- Hire from small salary
-- Step query
-- Use budget with Senior, use the remaining budget with junior

-- Compute cumulative sum of salary by experience from the smallest salary
with cte as (
  select
    employee_id,
    experience,
    sum(salary) over(
      partition by experience
      order by salary
    ) as rn
  from
    candidates
)

-- First use the budget with seniors
select
  employee_id
from
  cte
where
  experience = 'Senior'
  and rn < 70000

-- Then use the remaining budget to hire juniors
union

select
  employee_id
from
  cte
where
  experience = 'Junior'
  -- Find cumulative sum salary is less than 70000
  -- and its max is the amount of budget we used to hire senior
  -- So the below subtraction gives us the remaining budget to hire junior
  and rn < (
    select
      70000 - ifnull(max(rn), 0)
    from
      cte
    where
      experience = 'Senior'
      and rn < 70000
  )

;