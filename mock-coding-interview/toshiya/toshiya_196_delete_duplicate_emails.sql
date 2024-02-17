-- Write your PostgreSQL query statement below

-- with cte as (
--   select
--     id,
--     email,
--     row_number() over(
--       partition by email
--       order by id
--     ) as row_num
--   from
--     person
-- ),

-- cte2 as (
--   select
--     id
--   from
--     cte
--   where
--     row_num = 1
-- )

-- delete from
--   person
-- where
--   id not in (select id from cte2)
-- ;

delete from
  person as p1
using
  person as p2
where
  p1.Email = p2.Email
  and p1.Id > p2.Id
;
