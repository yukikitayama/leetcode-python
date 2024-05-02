-- Write your PostgreSQL query statement below
with cte as (
  select
    id,
    'Root' as type
  from
    tree
  where
    p_id is null
),

cte2 as (
  select
    id,
    'Inner' as type
  from
    tree
  where
    id in (
      select distinct p_id from tree
    )
    and p_id is not null
),

cte3 as (
  select
    id,
    'Leaf' as type
  from
    tree
  where
    id not in (
      select distinct p_id from tree where p_id is not null
    )
    and p_id is not null
)

select * from cte
union
select * from cte2
union
select * from cte3
;
