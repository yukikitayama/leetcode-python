-- Write your PostgreSQL query statement below

-- with cte as (
--   select
--     *,
--     percent_rank() over(
--       partition by state
--       order by fraud_score desc
--     ) as p_rank
--   from
--     fraud
-- )

-- select
--   policy_id,
--   state,
--   fraud_score
-- from
--   cte
-- where
--   p_rank <= 0.05
-- order by
--   2,
--   3 desc,
--   1
-- ;

with cte as (
  select
    *,
    -- row_number doesn't work for tie
    -- dense_rank doesn't work for this test case
    rank() over(
      partition by state
      order by fraud_score desc
    ) as rank
  from
    fraud
),

cte2 as (
  select
    state,
    count(policy_id) as num_policy
  from
    fraud
  group by
    1
)

select
  a.policy_id,
  a.state,
  a.fraud_score
from
  cte as a
left join
  cte2 as b
on
  a.state = b.state
where
  (a.rank - 1)::decimal / num_policy < 0.05
order by
  a.state,
  a.fraud_score desc,
  a.policy_id
;

