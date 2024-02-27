-- Write your PostgreSQL query statement below

-- with cte as (
-- select
--   school_id,
--   capacity,
--   student_count,
--   score,
--   case
--     when capacity >= student_count then 1
--     else 0
--   end as ok
-- from
--   schools as a,
--   exam as b
-- order by
--   school_id,
--   score desc
-- ),

-- cte2 as (
-- select
--   school_id,
--   min(score) as score
-- from
--   cte
-- where
--   ok = 1
-- group by
--   1
-- )

-- select
--   distinct a.school_id,
--   coalesce(b.score, -1) as score
-- from
--   schools as a
-- left join
--   cte2 as b
-- on
--   a.school_id = b.school_id
-- ;

select
  a.school_id,
  coalesce(min(b.score), -1) as score
from
  schools as a
left join
  exam as b
on
  a.capacity >= b.student_count
group by
  1
;