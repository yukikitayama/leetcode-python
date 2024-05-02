-- Write your PostgreSQL query statement below
with cte as (
  select
    N,
    'Root' as Type
  from
    tree
  where
    p is null
),

cte2 as (
  select
    N,
    'Leaf' as Type
  from
    tree
  where
    n not in (
      select distinct p from tree where p is not null
    )
    -- When there is only one node, without below condition, root node will also be leaf node
    and p is not null
),

cte3 as (
  select
    N,
    'Inner' as Type
  from
    tree
  where
    n in (
      select distinct p from tree where p is not null
    )
    and p is not null
)

select * from cte
union
select * from cte2
union
select * from cte3
order by N