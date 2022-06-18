with
-- Long format contest table
cte1 as (
  select
    gold_medal as user,
    contest_id
  from
    contests

  union all

  select
    silver_medal as user,
    contest_id
  from
    contests

  union all

  select
    bronze_medal as user,
    contest_id
  from
    contests
),

--
cte2 as (
  select
    user,
    contest_id,
    row_number() over(
      partition by user
      order by contest_id
    ) as rn
  from
    cte1
),

cte3 as (

  -- The user won any medal in three or more consecutive contests
  select
    user as user_id
  from
    cte2
  group by
    user,
    contest_id - rn
  having
    count(*) >= 3

  union all

  -- The user won the gold medal in three or more different contests (not necessarily consecutive)
  select
    gold_medal as user_id
  from
    contests
  group by
    gold_medal
  having
    count(*) >= 3
)

# select * from cte1;

-- This difference tells us consecutive win
-- select *, contest_id - rn from cte2;

select
  distinct b.name,
  b.mail
from
  cte3 as a
left join
  users as b
on
  a.user_id = b.user_id
;