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

## Date addition

`date_column + INTERVAL '1 DAY'` or `date_column + INTERVAL '1 day'`

`interval '1 day'` can be multiplied by number like `date_column - interval '1 day' * row_num`

https://www.sqlines.com/postgresql/how-to/dateadd

## Operator

`::` in PostgreSQL is a synonym for `CAST`, which converts a value into a different data type.

`CAST(integer_column as decimal)` is equal to `integer_column::decimal`

https://learnsql.com/blog/double-colon-operator-postgresql/

For not equal, both `<>` and `!=` will work.

For a value equal to null, `column_name IS NULL` will work.

## Type casting

- Integer to float
  - `integer_column::decimal`
- Integer to string
  - `integer_column::text`

https://stackoverflow.com/questions/13809547/convert-integer-to-string-in-postgresql

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

## If Null

MySQL `IFNULL()` doesn't exist in PostgreSQL. Use `COALESCE(expression, value_if_null)`. 
For example `coalesce(avg(column), 0)` returns 0 if `avg(column)` returns `NULL`.

## Outer join

In MySQL, by omitting `FULL`, `OUT JOIN` works, but PostgreSQL throws error. You need to write a complete `FULL OUTER JOIN` 
to perform outer join.

## String

`LOWER(string_column)` makes all the strings lowercase

## Concatenation

`CONCAT(string_or_colunm, string_or_colunm, string_or_colunm, ...)` works in PostgreSQL too.

Concatenating values in a column by `,` with MySQL `GROUP_CONCAT(column)` doesn't exist in PostgreSQL. Use `STRING_AGG()` instead

`STRING_AGG(expression, separator [order by column_name])`

`string_agg(numeric_column::text, ',' order by numeric_column::numeric)` when a column is `NUMERIC`, but we need to 
concatenate as `STRING` and concatenation should be ordered by the `NUMERIC` values. Need to add type casting.

https://www.postgresqltutorial.com/postgresql-aggregate-functions/postgresql-string_agg-function/

## Random sampling

MySQL `RAND()` doesn't exist in PostgreSQL. Instead, use `RANDOM()`

https://www.interviewquery.com/questions/random-sql-sample

## Delete

PostgreSQL lets you reference columns of other tables in the `WHERE` condition by specifying the other tables in the 
`USING` clause.

https://leetcode.com/problems/delete-duplicate-emails/description/
https://leetcode.com/problems/delete-duplicate-emails/solutions/4431290/postgresql/

```
DELETE FROM 
  films 
USING 
  producers
WHERE 
  producer_id = producers.id 
  AND producers.name = 'foo'
 ;
```

## Update

Swap update example. Use `CASE WHEN` and assign the result to `SET` value.

```sql
UPDATE
  table_name
SET
  column_name = case when column_a = 'female' then 'male' else 'female' end
;
```

## Format datetime to string

`to_char(timestamp_date_column, 'format_string')` converts timestamp/date column to a specific date format string.

To convert `2024-02-23` to year month format of `2024-02`, `to_char(date_column, 'YYYY-MM')`

https://www.postgresql.org/docs/8.1/functions-formatting.html

## Simple form of case expression

The CASE first evaluates the expression and compares the result with each value( value_1, value_2, …) in the WHEN clauses sequentially until it finds the match.

```sql
SELECT title,
       rating,
       CASE rating
           WHEN 'G' THEN 'General Audiences'
           WHEN 'PG' THEN 'Parental Guidance Suggested'
           WHEN 'PG-13' THEN 'Parents Strongly Cautioned'
           WHEN 'R' THEN 'Restricted'
           WHEN 'NC-17' THEN 'Adults Only'
       END rating_description
FROM film
ORDER BY title;
```
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-case/

## Modulo

`integer_column % 2 != 0` or `MOD(integer_column, 2) = 1` can find odd-number row.

`MOD(numerator, denominator)` or `MOD(dividend, divisor)`

https://www.postgresqltutorial.com/postgresql-math-functions/postgresql-mod/
