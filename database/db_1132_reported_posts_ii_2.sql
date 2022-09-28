with cte as (
select
  action_date,
  count(distinct b.post_id) / count(distinct a.post_id) as average
from
  actions as a
left join
  removals as b
on
  a.post_id = b.post_id
where
  a.extra = 'spam'
group by
  1
)

select
  round(avg(average) * 100, 2) as average_daily_percent
from
  cte
;