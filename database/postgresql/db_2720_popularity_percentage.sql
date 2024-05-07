/*
Find number of friends for each user
  union friends table with switch columns table
Find total number of users
  From above table, count distinct user IDs
Join two tables do math
*/

-- Write your PostgreSQL query statement below
with cte as (
  select
    user1,
    user2
  from
    friends
  union all
  select
    user2 as user1,
    user1 as user2
  from
    friends
)

select
  user1,
  round(
    count(distinct user2)::decimal / (select count(distinct user1) from cte) * 100,
    2
  ) as percentage_popularity
from
  cte
group by
  1
;
