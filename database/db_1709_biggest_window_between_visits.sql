select
  user_id,
  max(diff) as biggest_window
from (
select
  user_id,
  datediff(
    lead(visit_date, 1, '2021-01-01') over(
      partition by user_id
      order by visit_date
    ),
    visit_date
  ) as diff
from
  uservisits
) as a
group by
  user_id
order by
  user_id

;