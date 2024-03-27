# Write your MySQL query statement below
with cte as (
  select
    interview_id,
    sum(score) as total_score
  from
    rounds
  group by
    1
)

select
  a.candidate_id
from
  candidates as a
left join
  cte as b
on
  a.interview_id = b.interview_id
where
  a.years_of_exp >= 2
  and b.total_score > 15
;
