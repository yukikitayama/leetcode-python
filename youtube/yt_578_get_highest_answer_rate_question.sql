# Write your MySQL query statement below

with cte as (
  select
    question_id,
    rank() over(
      order by sum(if(action = 'answer', 1, 0)) / sum(if(action = 'show', 1, 0)) desc, question_id
    ) as rnk
  from
    surveylog
  group by
    1
)

select
  question_id as survey_log
from
  cte
where
  rnk = 1