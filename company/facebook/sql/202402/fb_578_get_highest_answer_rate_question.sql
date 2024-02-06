-- Write your PostgreSQL query statement below
/*
By question_id,
  count show
  count answer
  answer / show = answer_rate

Output smallest id by descending answer_rate
*/

with
show_count as (
select
  question_id,
  count(*) as show
from
  surveylog
where
  action = 'show'
group by
  1
),

answer_count as (
  select
    question_id,
    count(*) as answer
  from
    surveylog
  where
    action = 'answer'
  group by
    1
),

answer_rate as (
select
  a.question_id,
  b.answer::float / a.show as answer_rate
from
  show_count as a
inner join
  answer_count as b
on
  a.question_id = b.question_id

)

-- select * from answer_rate;

select
  question_id as survey_log
from
  answer_rate
order by
  answer_rate desc,
  question_id
limit
  1
;

-- with cte as (
--   select
--     question_id,
--     sum(case when action = 'show' then 1 else 0 end) as show,
--     sum(case when action = 'answer' then 1 else 0 end) as answer
--   from
--     surveylog
--   group by
--     1
-- )

-- select
--   question_id as survey_log
-- from
--   cte
-- order by
--   answer::decimal / show desc,
--   question_id
-- limit
--   1
-- ;


select
  question_id as survey_log
from
  surveylog
group by
  1
order by
  -- Use ::decimal to allow PostgreSQL to compute compute float division
  sum(case when action = 'answer' then 1 else 0 end)::decimal
  /
  sum(case when action = 'show' then 1 else 0 end) desc,
  question_id
limit
  1
;
