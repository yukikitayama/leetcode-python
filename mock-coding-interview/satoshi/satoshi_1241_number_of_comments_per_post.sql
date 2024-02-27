-- Write your PostgreSQL query statement below

with cte as (
  select
    parent_id as post_id,
    count(distinct sub_id) as number_of_comments
  from
    submissions
  where
    parent_id is not null
  group by
    1
)

select
  distinct a.sub_id as post_id,
  coalesce(b.number_of_comments, 0) as number_of_comments
from
  submissions as a
left join
  cte as b
on
  a.sub_id = b.post_id
where
  a.parent_id is null
;