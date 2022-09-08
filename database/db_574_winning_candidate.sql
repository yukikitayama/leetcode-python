with cte as (
  select
    candidateId
  from
    vote
  group by
    1
  order by
    count(distinct id) desc
  limit
    1
)

select
  a.name
from
  candidate as a
inner join
  cte as b
on
  a.id = b.candidateId
;
