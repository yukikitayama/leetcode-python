with
# cte1 as (
#   select
#     first_col,
#     row_number() over() as row_num
#   from
#     data
#   order by
#     1
# ),
# cte2 as (
#   select
#     second_col,
#     row_number() over() as row_num
#   from
#     data
#   order by
#     1 desc
# )
cte1 as (
  select
    first_col,
    row_number() over(order by first_col) as row_num
  from
    data
),
cte2 as (
  select
    second_col,
    row_number() over(order by second_col desc) as row_num
  from
    data
)

-- select * from cte2;

select
  a.first_col,
  b.second_col
from
  cte1 as a
left join
  cte2 as b
on
  a.row_num = b.row_num
;
