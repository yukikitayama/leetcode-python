-- Write your PostgreSQL query statement below

/*
union itself

self-join
  by a.user2_id = b.user2_id

a.user1_id < b.user2_id forms friendship

count a.user2_id by a.user1_id and b.user1_id
then output a.user1_id < b.user1_id
*/

with cte as (
  select
    user1_id,
    user2_id
  from
    friendship
  union
  select
    user2_id as user1_id,
    user1_id as user2_id
  from
    friendship
)

-- select * from cte order by 1, 2

select
  a.user1_id,
  b.user1_id as user2_id,
  count(distinct a.user2_id) as common_friend
from
  cte as a
full outer join
  cte as b
on
  a.user2_id = b.user2_id
where
  a.user1_id < b.user1_id
  -- Not only having at least 3 common friends,
  -- x and y needs to be a pair of friend
  and (a.user1_id, b.user1_id) in (
    select user1_id, user2_id from friendship
  )
group by
  1,
  2
having
  count(distinct a.user2_id) >= 3
;

