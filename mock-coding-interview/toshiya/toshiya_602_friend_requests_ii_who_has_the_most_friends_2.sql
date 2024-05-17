-- Write your PostgreSQL query statement below
with cte as (
  select
    requester_id,
    accepter_id
  from
    requestaccepted
  union all
  select
    accepter_id,
    requester_id
  from
    requestaccepted
)

select
  requester_id as id,
  count(accepter_id) as num
from
  cte
group by
  1
order by
  2 desc
limit
  1
;
