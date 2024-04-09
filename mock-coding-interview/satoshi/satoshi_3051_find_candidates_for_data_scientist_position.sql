# Write your MySQL query statement below
with cte as (
  select
    candidate_id,
    count(distinct skill) as cnt
  from
    candidates
  where
    skill in ("Python", "Tableau", "PostgreSQL")
  group by
    1
)

select
  candidate_id
from
  cte
where
  cnt = 3
order by
  1
;
