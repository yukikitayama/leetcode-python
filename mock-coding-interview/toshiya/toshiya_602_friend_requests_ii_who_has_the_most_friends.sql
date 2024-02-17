-- Write your PostgreSQL query statement below

with cte as (
  select
    requester_id,
    accepter_id
  from
    requestaccepted
  union all
  select
    accepter_id as requester_id,
    requester_id as accepter_id
  from
    requestaccepted
),

cte2 as (
  select
    requester_id,
    count(accepter_id) as num
  from
    cte
  group by
    requester_id
),

cte3 as (
  select
    requester_id,
    num,
    dense_rank() over(
      order by num desc
    ) as rnk
  from
    cte2
)

select
  requester_id as id,
  num
from
  cte3
where
  rnk = 1
;
