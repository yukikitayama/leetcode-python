# -- Pivot table
# select
#   b.item_category as category,
#   dayofweek(a.order_date) as day_of_week,
#   sum(quantity) as unit_ordered
# from
#   orders as a
# left join
#   items as b
# on
#   a.item_id = b.item_id
# group by
#   1,
#   2

# ;


-- Pivot table
select
  b.item_category as category,
  sum(case
    when dayofweek(a.order_date) = 2 then a.quantity
    else 0
  end) as monday,
  sum(case
    when dayofweek(a.order_date) = 3 then a.quantity
    else 0
  end) as tuesday,
  sum(case
    when dayofweek(a.order_date) = 4 then a.quantity
    else 0
  end) as wednesday,
    sum(case
    when dayofweek(a.order_date) = 5 then a.quantity
    else 0
  end) as thursday,
    sum(case
    when dayofweek(a.order_date) = 6 then a.quantity
    else 0
  end) as friday,
    sum(case
    when dayofweek(a.order_date) = 7 then a.quantity
    else 0
  end) as saturday,
    sum(case
    when dayofweek(a.order_date) = 1 then a.quantity
    else 0
  end) as sunday
from
  orders as a
-- Right join because the output table wants to have all the item_category
-- in the items table, and this items table will expand as one item_id in items is joined with multiple same item_id in orders
right join
  items as b
on
  a.item_id = b.item_id
group by
  1
order by
  1

;