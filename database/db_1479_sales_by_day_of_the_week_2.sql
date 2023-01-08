with
-- Aggregate quantity by category and day of week
cte1 as (
  select
    b.item_category,
    -- weekday starts with monday as 0 and ends with sunday as 6
    -- I prefer weekday to dayofweek because weekday allow us to separate weekend and non-weekend by '< 5'
    weekday(order_date) as day_of_week,
    sum(quantity) as unit
  from
    orders as a
  left join
    items as b
  on
    a.item_id = b.item_id
  group by
    1,
    2
),
-- Pivot a vertical table into a horizontal table by sum case when
cte2 as (
  select
    item_category,
    sum(case when day_of_week = 0 then unit else 0 end) as monday,
    sum(case when day_of_week = 1 then unit else 0 end) as tuesday,
    sum(case when day_of_week = 2 then unit else 0 end) as wednesday,
    sum(case when day_of_week = 3 then unit else 0 end) as thursday,
    sum(case when day_of_week = 4 then unit else 0 end) as friday,
    sum(case when day_of_week = 5 then unit else 0 end) as saturday,
    sum(case when day_of_week = 6 then unit else 0 end) as sunday
  from
    cte1
  group by
    1
)

select
  -- We need to show category even if no order happened
  -- so distinct to get all the categories and ifnull to show 0 when no order
  distinct a.item_category as Category,
  ifnull(b.monday, 0) as Monday,
  ifnull(b.tuesday, 0) as Tuesday,
  ifnull(b.wednesday, 0) as Wednesday,
  ifnull(b.thursday, 0) as Thursday,
  ifnull(b.friday, 0) as Friday,
  ifnull(b.saturday, 0) as Saturday,
  ifnull(b.sunday, 0) as Sunday
from
  items as a
left join
  cte2 as b
on
  a.item_category = b.item_category
order by
  1
;
