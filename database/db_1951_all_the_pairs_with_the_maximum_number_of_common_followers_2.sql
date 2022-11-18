with cte as (
  select
    a.user_id as user1_id,
    b.user_id as user2_id,
    count(*) as num_common_follower
  from
    relations as a,
    relations as b
  where
    a.follower_id = b.follower_id
    and a.user_id < b.user_id
  group by
    a.user_id,
    b.user_id
)

select
  user1_id,
  user2_id
from
  cte
where
  num_common_follower = (
    select max(num_common_follower) from cte
  )
;
