-- Create temporary table of number of participants by activity
with cte as (
select
  activity,
  count(id) as num_participant
from
  friends
group by
  activity
)

-- Find activities whose count is not either min or max
select
  activity
from
  cte
where
  -- Use subqueries to get min and max
  num_participant != (
    select
      min(num_participant)
    from
      cte
  )
  and num_participant != (
    select
      max(num_participant)
    from
      cte
  )
;
