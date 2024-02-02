# PostgreSQL

## If statement like MySQL

`IF` function doesn't exist in PostgreSQL. Instead, you need to use `CASE` like below

```
select
  case 
    when column_a = 0 then 0
    else column_b
  end as renamed_column_name
from
  table_name
 ```

## Operator

`::` in PostgreSQL is a synonym for `CAST`, which converts a value into a different data type.

`CAST(integer_column as decimal)` is equal to `integer_column::decimal`

https://learnsql.com/blog/double-colon-operator-postgresql/

## Division

`integer / integer` is integer division, so won't give you decimals

To produce decimals, you need to cast one of the variable to **float** or **decimal** like below

```
round(cast(num_accept as decimal) / cast(num_request as decimal), 2)

round(num_accept::decimal / num_request::decimal, 2)
```

https://stackoverflow.com/questions/34504497/division-not-giving-my-answer-in-postgresql
