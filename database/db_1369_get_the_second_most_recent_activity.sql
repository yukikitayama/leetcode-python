-- Use rank()?

select
  a.username,
  a.activity,
  a.startdate,
  a.enddate
from (
  select
    username,
    activity,
    startdate,
    enddate,
    row_number() over(
      partition by
        username
      order by
        startdate desc
    ) as 'rank',
    count(username) over(
      partition by
        username
    ) as 'count'
  from
    useractivity
) as a
where
  a.count = 1
  or a.rank = 2
;