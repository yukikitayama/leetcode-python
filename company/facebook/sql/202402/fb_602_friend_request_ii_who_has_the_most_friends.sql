-- Write your PostgreSQL query statement below

/*
Union
  swap r id and a id

Group by r id
  count a id
show top
*/

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
)

select
  requester_id  as id,
  count(accepter_id) as num
from
  cte
group by
  1
order by
  count(accepter_id) desc
limit
  1
;
