with cte as (
select
  a.account_id,
  year(a.day) * 12 + month(a.day) as day_id,
  if(sum(a.amount) > b.max_income, 1, 0) as exceed
from
  transactions as a
left join
  accounts as b
on
  a.account_id = b.account_id
where
  a.type = 'Creditor'
group by
  1,
  2
)

select
  distinct a.account_id
from
  cte as a,
  cte as b
where
  a.account_id = b.account_id
  and a.exceed = 1
  and b.exceed = 1
  and a.day_id = b.day_id - 1
;