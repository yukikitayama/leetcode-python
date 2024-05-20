-- Write your PostgreSQL query statement below
with cte as (
  select
    a.name,
    sum((b.id is not null)::integer) as num_participants
  from
    activities as a
  left join
    friends as b
  on
    a.name = b.activity
  group by
    1
)

select
  name as activity
from
  cte
where
  num_participants != (
    select min(num_participants) from cte
  )
  and num_participants != (
    select max(num_participants) from cte
  )
;