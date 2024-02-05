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

## Date difference

PostgreSQL doesn't have `DATEDIFF` of MySQL, so you need to use `DATE_PART()` with the following syntax. `DATE` column 
needs to be converted to `timestamp`.
```
DATE_PART('day', later_date_column::timestamp - earlier_date_column::timestamp)
```

- https://leetcode.com/problems/active-users/solutions/4668692/postgresql-solution-with-date-part/
- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/solutions/4669355/postgresql-solution-with-date-part/

## Operator

`::` in PostgreSQL is a synonym for `CAST`, which converts a value into a different data type.

`CAST(integer_column as decimal)` is equal to `integer_column::decimal`

https://learnsql.com/blog/double-colon-operator-postgresql/

For not equal, both `<>` and `!=` will work.

For a value equal to null, `column_name IS NULL` will work.

## Division

`integer / integer` is integer division, so won't give you decimals

To produce decimals, you need to cast one of the variable to **float** or **decimal** like below

```
round(cast(num_accept as decimal) / cast(num_request as decimal), 2)

round(num_accept::decimal / num_request::decimal, 2)
```

https://stackoverflow.com/questions/34504497/division-not-giving-my-answer-in-postgresql

When you have 2 integer columns and we want the division to produce float, use `integer_column_a::decimal / integer_column_b`

## Average

PostgreSQL `AVG(integer_column_name)` produces **floating-point** number, even if the input is integers. So no need for 
type conversion like `::decimal` to access decimals.

## Single quote and double quote

In PostgreSQL, you cannot use double quote `"string"` to have string constants. You need to use single quote like 
`'string'`. 

Double quotes are used for table names or field names, but you can omit. Most verbose query is below

```
seelct * 
from "table_name" 
where "string_column_name" = 'something'
;
```

https://stackoverflow.com/questions/41396195/what-is-the-difference-between-single-quotes-and-double-quotes-in-postgresql

## GROUP BY HAVING

PostgreSQL `GROUP BY HAVING` is different from MySQL. In `SELECT` statement, you cannot have additional columns which 
don't appear in `GROUP BY`. People say, for this part, MySQL is more relaxed than PostgreSQL.
