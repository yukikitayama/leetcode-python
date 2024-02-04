with cte as (
  select
    *,
    id - row_number() over(
      partition by num
      order by id
    ) as group_id
  from
    logs
)

select
  distinct num as consecutivenums
from
  cte
group by
  num,
  group_id
having
  count(group_id) >= 3
;
