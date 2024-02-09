-- Write your PostgreSQL query statement below

/*
Query
  Group by query_name average
    rating divided by position
    count of rating less than 3 divide by the number of ratings
*/

with cte as (
  select
    *,
    case
      when rating < 3 then 1
      else 0
    end as poor_count
  from
    queries
)

-- select * from cte;

select
  query_name,
  round(avg(rating::decimal / position), 2) as quality,
  round(sum(poor_count)::decimal / count(rating) * 100, 2) as poor_query_percentage
from
  cte
where
  query_name is not null
group by
  1
;
