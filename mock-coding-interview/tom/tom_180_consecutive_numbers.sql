-- Write your PostgreSQL query statement below

/*
with cte as (
  select
    *,
    row_number() over(
      partition by num
      order by id
    ) as row_num
  from
    logs
),

cte2 as (
  select
    id - row_num as group_id,
    num
  from
    cte
),

cte3 as (
  select
    group_id,
    num,
    count(*) as cnt
  from
    cte2
  group by
    1,
    2
)

-- select * from cte2;
-- select * from cte3;
-- select * from cte3 where cnt >= 3;

select
  distinct num as ConsecutiveNums
from
  cte2
where
  (group_id, num) in (
select
  group_id, num as ConsecutiveNums
from
  cte3
where
  cnt >= 3
  )
;
*/

select
  distinct a.num as consecutivenums
from
  logs as a,
  logs as b,
  logs as c
where
  a.id = b.id - 1
  and a.id = c.id - 2
  and a.num = b.num
  and a.num = c.num
;

