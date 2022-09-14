with
cte1 as (
  select
    requester_id as id1,
    accepter_id as id2
  from
    requestaccepted
  union all
  select
    accepter_id as id1,
    requester_id as id2
  from
    requestaccepted
),
cte2 as (
  select
    id1 as id,
    count(distinct id2) as num
  from
    cte1
  group by
    1
)

select
  *
from
  cte2
where
  num = (select max(num) from cte2)
;
