with cte as (
  select
    -- Explanation multiplies by 2 and divided the doubled row numbers,
    -- so actually we don't need to multiply and use the original number of rows
    avg(duration) as global_average
  from
    calls
)

select
  b.name as country
from
  person as a
join
  country as b
on
  left(a.phone_number, 3) = b.country_code
join
  calls as c
on
  -- Calls count when it appears either caller_id or callee_id
  -- So this join inflates the number of rows of calls table.
  -- e.g. duration 33 can be obtained 2 times when a.id is 1 and a.id is 9
  a.id = c.caller_id
  or a.id = c.callee_id
group by
  b.name
having
  avg(c.duration) > (select global_average from cte)
;
