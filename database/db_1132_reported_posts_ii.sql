-- number of ids which are removed / number of ids which are reported as spam

-- Compute overall average
select
  round(
    sum(d.daily_avg) / count(d.date) * 100,
    2
  ) as average_daily_percent
from (
select
  c.action_date as date,
  -- Number of removed divided by number of spam reports
  count(distinct
    case
      when remove_date is not null then post_id
      else null
    end
  ) / count(
    distinct post_id
  ) as daily_avg
from (
select
  a.post_id,
  a.action_date,
  b.remove_date
from
  actions as a
left join
  removals as b
on
  a.post_id = b.post_id
where
  a.extra = 'spam'
) as c
group by
  1
) as d

;
