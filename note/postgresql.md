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

`DATE_PART()` requires single quotations to unit, unlike `EXTRACT()`

- https://leetcode.com/problems/active-users/solutions/4668692/postgresql-solution-with-date-part/
- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/solutions/4669355/postgresql-solution-with-date-part/

## Date addition

`date_column + INTERVAL '1 DAY'` or `date_column + INTERVAL '1 day'`

`interval '1 day'` can be multiplied by number like `date_column - interval '1 day' * row_num`

https://www.sqlines.com/postgresql/how-to/dateadd, read section "Adding Interval from Variable or Column"

If we have `date` type column and add number of days dynamically with another column of addition, and the output column
still needs to be `date` type, do following, because interval addition returns `timestamp` type.

`(date_column + num_days_integer_column * interval '1 day')::date`

- [2701. Consecutive Transactions with Increasing Amounts](https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/description/)

## Extract hour from timestamp

You can extract hour from timestamp by `extract(hour from timestamp_column)`

`EXTRACT()` doesn't require single quotation to unit, unlike `DATE_PART()`

- [2984. Find Peak Calling Hours for Each City](https://leetcode.com/problems/find-peak-calling-hours-for-each-city/description/)

## Get day of week

`extract(dow from date_column)`. Use `dow`. Sunday is 0. Saturday is 6.

- [3118. Friday Purchase III ](https://leetcode.com/problems/friday-purchase-iii/description/)

## Get integer representing week of year

`extract(week from date_column)`.

- [3118. Friday Purchase III ](https://leetcode.com/problems/friday-purchase-iii/description/)

## Datetime or timestamp

There is no `datetime` in PostgreSQL. There's `timestamp`.

https://stackoverflow.com/questions/15501734/how-to-convert-date-to-datetime-in-postgresql

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

### Column names with spaces

The below is valid. https://leetcode.com/problems/total-traveled-distance/description/

```
-- Write your PostgreSQL query statement below
with cte as (
  select
    user_id,
    sum(distance) as "traveled distance"
  from
    rides
  group by
    1
)

select
  a.user_id,
  a.name,
  coalesce(b."traveled distance", 0) as "traveled distance"
from
  users as a
left join
  cte as b
on
  a.user_id = b.user_id
order by
  1
;
```

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

To substring from a particular character position use `SUBSTRING()` and `POSITION(char IN column)`. For example, to extract email domain,
`SUBSTRING(email_column, POSITION('@' IN email_column) + 1)`

- [3059. Find All Unique Email Domains](https://leetcode.com/problems/find-all-unique-email-domains/description/)

### Convert number to string

`integer_column::text`. User `::text`, not `::string`.

## Convert number of seconds to formatted string

`to_char((number_of_seconds::text || 'second')::interval, 'HH24:MI:SS') as duration_formatted`

https://stackoverflow.com/questions/2905692/postgresql-how-to-convert-seconds-in-a-numeric-field-to-hhmmss

https://www.postgresqltutorial.com/postgresql-string-functions/postgresql-to_char/

- [3124. Find Longest Calls](https://leetcode.com/problems/find-longest-calls/description/)

## LIKE

`%` can capture one or more characters, so to filer emails with domains ending with `.com`, you can use `email_column LIKE '%@%.com'`

- [3059. Find All Unique Email Domains](https://leetcode.com/problems/find-all-unique-email-domains/description/)

## Concatenation

`CONCAT(string_or_colunm, string_or_colunm, string_or_colunm, ...)` works in PostgreSQL too.

Concatenating values in a column by `,` with MySQL `GROUP_CONCAT(column)` doesn't exist in PostgreSQL. Use `STRING_AGG()` instead

`STRING_AGG(expression, separator [order by column_name])`

`string_agg(numeric_column::text, ',' order by numeric_column::numeric)` when a column is `NUMERIC`, but we need to 
concatenate as `STRING` and concatenation should be ordered by the `NUMERIC` values. Need to add type casting.

https://www.postgresqltutorial.com/postgresql-aggregate-functions/postgresql-string_agg-function/

`string || string`, `||` can work as a concatenation operator.

- [3124. Find Longest Calls](https://leetcode.com/problems/find-longest-calls/description/)

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

## Sum of boolean

In MySQL you can sum of boolean like `sum(number_column < 5)` but it doesn't work in PostgreSQL. It needs type conversion.

`sum((rating < 3)::integer)` works.

## Percentile

`PERCENT_RANK()` returns 0% to 100% percentage ranking. Top has 0 and bottom has 1.

- [3055. Top Percentile Fraud](https://leetcode.com/problems/top-percentile-fraud/description/)

https://www.postgresqltutorial.com/postgresql-window-function/postgresql-percent_rank-function/

## Regular expression to substring

Extract hashtag from a tweet (Assuming one tweet contains exactly one hashtag and hashtag is consisted of lower and upper case letters only) 
`REGEXP_SUBSTR(tweet_column, '#[a-zA-Z]+')`

- [3087. Find Trending Hashtags](https://leetcode.com/problems/find-trending-hashtags/description/)

## Get length of string contents in a string column

`length(string_column)`

- [3150. Invalid Tweets II](https://leetcode.com/problems/invalid-tweets-ii/description/)

## Count the number of occurrence of a certain character in string column

`length(string_column) - length(replace(string_column, '@', ''))`

`length(string_column) - length(replace(string_column, '#', ''))`

- [3150. Invalid Tweets II](https://leetcode.com/problems/invalid-tweets-ii/description/)

## RANGE BETWEEN in order by of window function

```
-- Compute how many posts were made in 7 window for each date
cte3 as (
  select
    user_id,
    post_date,
    count(*) over(
      partition by user_id
      -- 6 without single quotation doesn't work in PostgreSQL 
      order by post_date range between interval '6' day preceding and current row
    ) as count_7window
  from
    cte
),
```

- [3089. Find Bursty Behavior](https://leetcode.com/problems/find-bursty-behavior/description/)

https://learnsql.com/blog/range-clause/

https://www.postgresqltutorial.com/postgresql-window-function/

https://www.geeksforgeeks.org/frame-clause-in-sql/