with cte as (
  select
    *
  from (
    select
      a.seller_id,
      rank() over(
        partition by a.seller_id
        order by a.order_date
      ) as rk,
      b.item_brand
    from
      orders as a
    inner join
      items as b
    on
      a.item_id = b.item_id
  ) as c
  where
    rk = 2
)

select
  user_id as seller_id,
  case
    when d.favorite_brand = e.item_brand then 'yes'
    else 'no'
  end as '2nd_item_fav_brand'
from
  users as d
left join
  cte as e
on
  d.user_id = e.seller_id
;
