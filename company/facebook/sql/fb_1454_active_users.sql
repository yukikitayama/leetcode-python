-- Write your PostgreSQL query statement below
with

cte as (
    select
        a.id,
        a.login_date as origin_date,
        b.login_date as following_date
    from
        logins as a
    join
        logins as b
    on
        a.id = b.id
        -- Find dates which can connect 4 other dates with the below condition
        -- If 4 dates are connected, thie particular date has 4 consecutive dates
        and date_part('day', b.login_date::timestamp - a.login_date::timestamp) between 1 and 4
    left join
        accounts as c
    on
        a.id = c.id
),

-- Count how many consecutive days from origin_date
cte2 as (
  select
    id,
    origin_date,
    count(distinct following_date) as num
  from
    cte
  group by
    1,
    2
)

-- select * from cte order by 1, 2, 3;
-- select * from cte2;

-- Get name and show only id which has consecutive and following 4 days
select
  distinct a.id,
  b.name
from
  cte2 as a
left join
  accounts as b
on
  a.id = b.id
where
  a.num = 4
order by
  1
;