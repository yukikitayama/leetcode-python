/*
id  asc desc    desc-1  desc+1
a   1   5       4       6
b   2   4       3       5
c   3   3       2       4
d   4   2       1       3
e   5   1       0       2

*/

select
  id,
  company,
  salary
from (

select
  id,
  company,
  salary,
  row_number() over(
    partition by company
    order by salary, id
  ) as row_num_asc,
  row_number() over(
    partition by company
    order by salary desc, id desc
  ) as row_num_desc
from
  employee

) as a

where
  row_num_asc between row_num_desc - 1 and row_num_desc + 1

;