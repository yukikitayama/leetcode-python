-- with
-- apple as (
--   select
--     sale_date,
--     sold_num
--   from
--     sales
--   where
--     fruit = 'apples'
-- ),

-- orange as (
--   select
--     sale_date,
--     sold_num
--   from
--     sales
--   where
--     fruit = 'oranges'
-- )

-- select
--   a.sale_date,
--   a.sold_num - b.sold_num as diff
-- from
--   apple as a
-- left join
--   orange as b
-- on
--   a.sale_date = b.sale_date
-- order by
--   1
-- ;

select
  sale_date,
  sum(
    case
      when fruit = 'apples' then sold_num
      else -sold_num -- This is orange
    end
  ) as diff
from
  sales
group by
  1
order by
  1
;