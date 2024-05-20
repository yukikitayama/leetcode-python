-- Write your PostgreSQL query statement below
select
  problem_id
from
  problems
where
  likes::decimal / (likes + dislikes) < 0.6
order by
  1