# Write your MySQL query statement below
select
  a.visited_on as visited_on,
  sum(b.day_sum) as amount,
  round(avg(b.day_sum), 2) as average_amount

# Make cartesian product rows
from
 (
select
  visited_on,
  sum(amount) as day_sum
from
  customer
group by
  visited_on
 ) as a,
 (
select
  visited_on,
  sum(amount) as day_sum
from
  customer
group by
  visited_on
 ) as b

# But limit only within 7 days
where
  datediff(a.visited_on, b.visited_on) between 0 and 6

# Group by to compute stats by day
group by
  a.visited_on

# a.visited_on is fixed, but b.visited_on increments
# so count(b.visited_on) = 7 is the group by stats using 7 days data
having
  count(b.visited_on) = 7

order by
  a.visited_on
;
