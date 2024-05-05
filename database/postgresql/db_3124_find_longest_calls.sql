-- Write your PostgreSQL query statement below

-- with cte as (
--   select
--     b.first_name,
--     a.type,
--     a.duration,
--     dense_rank() over(
--       partition by a.type
--       order by a.duration desc
--     ) as d_rank
--   from
--     calls as a
--   left join
--     contacts as b
--   on
--     a.contact_id = b.id
-- )

-- select
--   first_name,
--   type,
--   to_char((duration::text || 'second')::interval, 'HH24:MI:SS') as duration_formatted
-- from
--   cte
-- where
--   d_rank <= 3
-- order by
--   type,
--   duration_formatted desc,
--   first_name desc
-- ;

with cte as (
  select
    b.first_name,
    a.type,
    duration / 3600 as hour,
    case when duration / 60 > 60 then duration / 60 % 60 else duration / 60 end as minute,
    duration % 60 as second,
    dense_rank() over(
      partition by a.type
      order by a.duration desc
    ) as d_rank
  from
    calls as a
  left join
    contacts as b
  on
    a.contact_id = b.id
)


select
  first_name,
  type,
  concat(
    -- Hour
    case when hour < 10 then '0' || hour::text else hour::text end,
    ':',
    -- Minute
    case when minute < 10 then '0' || minute::text else minute::text end,
    ':',
    -- Second
    case when second < 10 then '0' || second::text else second::text end
  ) as duration_formatted
from
  cte
where
  d_rank <= 3
order by
  type,
  duration_formatted desc,
  first_name desc
;
