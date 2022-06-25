with cte as (
-- Cumulative sum of salary by experience
select
  employee_id,
  experience,
  sum(salary) over(
    partition by experience
    order by salary, employee_id
  ) as cumsum_salary
from
  candidates
)

select
  'Senior' as experience,
  count(*) as accepted_candidates
from
  cte
where
  experience = 'Senior'
  and cumsum_salary <= 70000

union

select
  'Junior' as experience,
  count(*) as accepted_candidates
from
  cte
where
  experience = 'Junior'
  and cumsum_salary < (
    -- Find biggest cumsum_salary below 70000 in senior group
    -- so the different between this biggest amount and 70000
    -- is the remaining budget for junior
    select
      70000 - ifnull(max(cumsum_salary), 0)
    from
      cte
    where
      experience = 'Senior'
      and cumsum_salary <= 70000
  )
;
