with
cte1 as (
  select
    a.id
  from
    trips as a
  left join
    users as b
  on
    a.client_id = b.users_id
  where
    b.banned = "Yes"
),
cte2 as (
  select
    a.id
  from
    trips as a
  left join
    users as b
  on
    a.driver_id = b.users_id
  where
    b.banned = "Yes"
)

-- select * from cte1;
-- select * from cte1;

select
  request_at as Day,
  round(sum(status != "completed") / count(status), 2) as "Cancellation Rate"
from
  trips
where
  request_at between "2013-10-01" and "2013-10-03"
  and id not in (select * from cte1)
  and id not in (select * from cte2)
group by
  1
;