select
  question_id as survey_log
from (
select
  question_id,
  sum(case when action = 'show' then 1 else 0 end) as num_show,
  sum(case when action = 'answer' then 1 else 0 end) as num_answer
from
  surveylog
group by
  question_id
) as a
order by
  a.num_answer / a.num_show desc,
  question_id
limit
  1

;