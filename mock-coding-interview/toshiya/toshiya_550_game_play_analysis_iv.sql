# Write your MySQL query statement below
with cte as (
  select
    player_id,
    min(event_date) as first_date
  from
    activity
  group by
    1
),

cte2 as (
  select
    a.player_id,
    datediff(a.event_date, b.first_date) as diff
  from
    activity as a
  left join
    cte as b
  on
    a.player_id = b.player_id
)

-- select * from cte2;

select
  round(
  (select count(distinct player_id) from cte2 where diff = 1)
  /
  (select count(distinct player_id) from cte2)
  , 2
  ) as fraction
;