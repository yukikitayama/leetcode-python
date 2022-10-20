select
  sale_date,
  sum(if(fruit = 'apples', sold_num, -sold_num)) as diff
from
  sales
group by
  1
order by
  1
;