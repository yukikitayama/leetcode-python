-- Count the number of followers for each followee
with
cte1 as (
  select
    followee,
    count(distinct follower) as num
  from
    follow
  group by
    1
)

select
-- distinct to remove duplicated followee
  distinct a.followee as follower,
  a.num
from
  cte1 as a
-- Inner join to filter out the users who don't follow anybody
inner join
  follow as b
on
  a.followee = b.follower
order by
  1
;