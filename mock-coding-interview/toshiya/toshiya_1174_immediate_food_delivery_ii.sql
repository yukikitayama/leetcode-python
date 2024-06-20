/*
cust_id date  row_num
1       08-01 1
1       08-02 2
2       09-01 1
2       09-02 2
3       09-02 1
*/

-- Write your PostgreSQL query statement below
with cte as (
  select
    customer_id,
    order_date,
    customer_pref_delivery_date,
    row_number() over(
      partition by customer_id
      order by order_date
    ) as row_num
  from
    delivery
)

select
  round(
    100 * sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)::decimal
    /
    count(*),
    2
  ) as immediate_percentage
from
  cte
where
  row_num = 1
;