with cte as (
  select
    a.user_id as user1_id,
    b.user_id as user2_id,
    count(distinct a.follower_id) as common
  from
    relations as a
  join
    relations as b
  on
    a.user_id < b.user_id
    and a.follower_id = b.follower_id
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
  common = (
    select
      max(common)
    from
      cte
  )
;
