with
-- Assign group ID to rows which have consecutive IDs
cte1 as (
select
  *,
  id - row_number() over(order by id) as group_id
from
  stadium
where
  people >= 100
),
-- Find group ID which has three or more rows
cte2 as (
  select
    group_id
  from
    cte1
  group by
    group_id
  having
    count(*) >= 3
)

select
  id,
  visit_date,
  people
from
  cte1
where
  group_id in (
    select * from cte2
  )
order by
  2
;