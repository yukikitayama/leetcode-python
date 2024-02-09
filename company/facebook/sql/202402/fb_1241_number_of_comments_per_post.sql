-- Write your PostgreSQL query statement below

/*
self join
  sub_id as post_id
  sub_id = parant_id to left join
  count distinct joined sub_id group by post_id
    when count is null, replace it with 0
*/

select
  a.sub_id as post_id,
  coalesce(count(distinct b.sub_id), 0) as number_of_comments
from
  submissions as a
left join
  submissions as b
on
  a.sub_id = b.parent_id
where
  a.parent_id is null
group by
  a.sub_id
order by
  1
;
