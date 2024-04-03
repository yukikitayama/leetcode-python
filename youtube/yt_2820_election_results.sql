# Write your MySQL query statement below
with cte as (
  select
    voter,
    1 / count(distinct candidate) as weight
  from
    votes
  where
    candidate is not null
  group by
    1
),

cte1 as (
  select
    a.candidate,
    ifnull(b.weight, 0) as weight
  from
    votes as a
  left join
    cte as b
  on
    a.voter = b.voter
),

cte2 as (
  select
    candidate,
    sum(weight) as total_weight
  from
    cte1
  group by
    candidate
)

select
  candidate
from
  cte2
where
  total_weight = (
    select max(total_weight) from cte2
  )
order by
  candidate
;