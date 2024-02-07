-- Write your PostgreSQL query statement below

/*
Percentage
  num removed / num spam post

Num spam post
  count distinct post_id by date extra is spam

Num removed
  Join removal to actions and daily count of removals remove_date

Query
  Join actions and removals
    Actions only extra is spam
    On post_id
  Group by action_date
    removals post_id / actions post_id

  Put above to CTE

  average those rate
*/

with cte as (
  select
    a.action_date,
    count(distinct b.post_id)::decimal / count(distinct a.post_id) as removal_rate
  from
    actions as a
  left join
    removals as b
  on
    a.post_id = b.post_id
  where
    a.extra = 'spam'
  group by
    a.action_date
)

-- select * from cte;

select
  round(avg(removal_rate) * 100, 2) as average_daily_percent
from
  cte
;