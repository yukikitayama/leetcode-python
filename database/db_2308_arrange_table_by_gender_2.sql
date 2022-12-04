-- Precomute orders
with cte as (
  select
    user_id,
    gender,
    -- Assign order for each gender
    case
      when gender = 'female' then 1
      when gender = 'other' then 2
      else 3
    end as gender_order,
    -- Assign order by user_id within each gender
    row_number() over(
      partition by gender
      order by user_id
    ) as order_within_gender
  from
    genders
)

select
  user_id,
  gender
from
  cte
order by
  -- First arrange the rows of low user_id within gender to the top
  order_within_gender,
  -- And reorder them by gender order so female will be the first
  gender_order
;