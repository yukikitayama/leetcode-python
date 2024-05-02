# Write your MySQL query statement below
with cte as (
  select
    user_id,
    spend,
    transaction_date,
    row_number() over(
      partition by user_id
      order by transaction_date
    ) as row_num
  from
    transactions
)

select
  a.user_id,
  a.spend as third_transaction_spend,
  a.transaction_date as third_transaction_date
from
  cte as a
left join
  cte as b
on
  a.user_id = b.user_id
  and a.row_num = b.row_num + 1
left join
  cte as c
on
  a.user_id = c.user_id
  and a.row_num = c.row_num + 2
where
  a.row_num = 3
  and a.spend > b.spend
  and a.spend > c.spend
;
