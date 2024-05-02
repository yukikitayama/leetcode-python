# SQL

- Filter records which have missing
  - `WHERE column_name IS NULL`
- If a value in a column is null, replace with something
  - `IFNULL(column_name, 0)` e.g. Replace with 0 if it's missing
- Create a new column based on the other column value
  - [1435. Create a Session Bar Chart](https://leetcode.com/problems/create-a-session-bar-chart/)
```
CASE 
  WHEN condition_from_other_column THEN value
  WHEN condition_from_other_column THEN value
  ELSE value
END
```
- Make a new table without `FROM`
  - Use `SELECT` and `UNION ALL`. e.g. The below makes a table with one column 'col' with values 'a' and 'b' for each 
    row.
  - [1435. Create a Session Bar Chart](https://leetcode.com/problems/create-a-session-bar-chart/)
```
SELECT 'a' AS col
UNION ALL
SELECT 'b' AS col
```

## CONCAT()

- `CONCAT` concatenates **horizontally from multiple columns**.
  - https://www.w3schools.com/sql/func_mysql_concat.asp
- `CONCAT(exp1, exp2, ...)` concatenate two or more expressions
- Expression can be either string or even string. The result is string.
- Doesn't specify `separator` string. If you wanna separate each expression by `,` or ` ` (space), use `GROUP_CONCAT()`

## GROUP_CONCAT()

- `GROUP_CONCAT` concatenates **vertically from single column**.
  - https://www.geeksforgeeks.org/mysql-group_concat-function/
- Concatenate string from a group into a single string with options such as separator.
- e.g. `GROUP_CONCAT(DISTINCT col ORDER BY col separator ',')`
  - `seperator ','` can be omitted because by default ',' is a separator.
- By default, maximum length of returned string by `GROUP_CONCAT()` is set to `1024` in MYSQL. If we wanna make it 
  longer, run this
  - `SET SESSION group_concat_max_len = 1000000;`
  - [5.1.7 Server System Variables](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html)
- [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/)
- [2118. Build the Equation](https://leetcode.com/problems/build-the-equation/)
- [MySQL GROUP_CONCAT Function](https://www.mysqltutorial.org/mysql-group_concat/)
- [2199. Finding the Topic of Each Post](https://leetcode.com/problems/finding-the-topic-of-each-post/)
- [2252. Dynamic Pivoting of a Table](https://leetcode.com/problems/dynamic-pivoting-of-a-table/)

## Percentage

- Use `AVG()` and `CASE WHEN` to convert a column into binary
- [SQL 1 liner solution (This is a FB DE interview question)](https://leetcode.com/problems/recyclable-and-low-fat-products/discuss/1062936/SQL-1-liner-solution-(This-is-a-FB-DE-interview-question))

```sql
select
  round(
    avg(
      case when column = 'something' 
        then 1 
        else 0 
      end), 
    2) 
  as percentage
from
  some_table
```

## IS NULL for 3-Valued Logic

- MySQL uses 3-valued logic, `TRUE`, `FALSE`, and `UNKNOWN`
- Anything compared to `NULL` evaluates to the 3rd value `UNKNOWN`
- For example, `where column != 1` only returns rows which have non-null value and not 1
  - If a row has null in the column, this row will not be returned.
  - If we wanna return this null row as well, `where column != 1 or column is null`
- [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)

## If Statement

- `select if(condition, true, false) as name`
- [873. Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/)

## Case When

- 2 ways to construct `case when` syntax.
- [13.6.5.1 CASE Statement](https://dev.mysql.com/doc/refman/5.7/en/case.html)
- [627. Swap Salary](https://leetcode.com/problems/swap-salary/)

## Delete

- [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)

## LIKE

- [1527. Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/)
- [2199. Finding the Topic of Each Post](https://leetcode.com/problems/finding-the-topic-of-each-post/)
  - `ON CONCAT(something, something) LIKE CONCAT(something, something)`

## LIMIT

- `LIMIT 1 OFFSET 1` allows us to get the only second element, because `OFFSET 1` skips the first row
- [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)
- [MySQL LIMIT](https://www.mysqltutorial.org/mysql-limit.aspx)
- [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/)

## IFNULL

- [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

## Optimization

- [1581. Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)
  - [simple MySQL solution (Visits.visit_id not in (SELECT visit_id FROM Transactions))](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/discuss/841000/simple-MySQL-solution-(Visits.visit_id-not-in-(SELECT-visit_id-FROM-Transactions)))
  - Comments in the above discussion discuss why `LEFT JOIN` is better than `NOT IN` subquery in this problem
  - Sub query runs earlier than main query.
  - Subquery returns a list and in where clause for each item checks against the list, so not optimized

```sql
# Write your MySQL query statement below
# select
#   customer_id,
#   count(*) as count_no_trans
# from
#   visits
# where
#   visit_id not in (
#     select visit_id from transactions
#   )
# group by
#   customer_id
# ;

select
  a.customer_id,
  count(a.visit_id) as count_no_trans
from
  visits as a
left join
  transactions as b
on
  a.visit_id = b.visit_id
where
  b.transaction_id is null
group by
  a.customer_id
```

## DATEDIFF()

- `DATEDIFF(later_date, earlier_date)`
- This can be used in where clause like `where datediff(later_date, earlier_date) = 1` to find yesterday data.
- [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/)
- [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)

## Having

- Add a condition to a `GROUP BY` result
- [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)
- [1050. Actors and Directors Who Cooperated At Least Three Times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)

## DATE_FORMAT

- Create `YYYY-MM` by `DATE_FORMAT(date_column, '%Y-%m')`.
- [615. Average Salary: Departments VS Company](https://leetcode.com/problems/average-salary-departments-vs-company/description/)
- `DATE_FORMAT(DATE, 'FORMAT_STRING')`
- `%m`: month `00` to `12`
- `%Y`: 4 digits year
- `%W`: Weekday name in full (Sunday to Saturday)
- `%M`: Month name in full (January to December)
- `%e`: Day of the month as a numeric value without leading 0
  - `1`, not `01`
  - If `01` is required, use `%d`
- [1853. Convert Date Format](https://leetcode.com/problems/convert-date-format/)
- [MySQL DATE_FORMAT() Function](https://www.w3schools.com/sql/func_mysql_date_format.asp)

## 2 Items for NOT IN

- `WHERE (column1, column2) NOT IN (column1, column2)` can work
- [1112. Highest Grade For Each Student](https://leetcode.com/problems/highest-grade-for-each-student/)

## MOD

- `MOD(dividend (numerator), divisor (denominator))` returns `remainder` of a number divided by another number

## Common Table Expression

- [13.2.15 WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html)
- Multiple common table expressions
  - If table contains both recursive and non-recursive, put `RECURSIVE` right after `WITH`

## Rank

- `order by` can use `desc` after column name

```
rank() over(
  partition by
    WITHIN-GROUP_TO_ASSIGN_RANK
  order by
    COLUMN_TO_REFER_TO_MAKE_RANK 
) as RANK_COLUMN_NAME
```

## DENSE_RANK() vs RANK()

- [MySQL DENSE_RANK Function](https://www.mysqltutorial.org/mysql-window-functions/mysql-dense_rank-function/)
- `DENSE_RANK()` returns **consecutive rank**, but `RANK()` will skip a number when a tie exists.

## Recursive Common Table Expression (Recursive CTE)

- If table contains both recursive and non-recursive, put `RECURSIVE` right after `WITH` (before the first cte name), 
  even if the first CTE isn't for recursive, and the second cte is for recursive.
- A common table expression using `with recursive` and having a subquery inside referring to its own table
- [1336. Number of Transactions per Visit](https://leetcode.com/problems/number-of-transactions-per-visit/description/)
- [1384. Total Sales Amount by Year](https://leetcode.com/problems/total-sales-amount-by-year/)
- [1613. Find the Missing IDs](https://leetcode.com/problems/find-the-missing-ids/)
- [1635. Hopper Company Queries I](https://leetcode.com/problems/hopper-company-queries-i/description/)
- [1645. Hopper Company Queries II](https://leetcode.com/problems/hopper-company-queries-ii/description/)
- [1651. Hopper Company Queries III](https://leetcode.com/problems/hopper-company-queries-iii/description/)
- [1767. Find the Subtasks That Did Not Execute](https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/description/)
- [Recursive Common Table Expressions](https://dev.mysql.com/doc/refman/8.0/en/with.html#common-table-expressions-recursive)
- [Generate an integer sequence in MySQL](https://stackoverflow.com/questions/304461/generate-an-integer-sequence-in-mysql)
- [[MySQL] 4 solutions to generate consecutive sequence](https://leetcode.com/problems/find-the-missing-ids/discuss/890608/MySQL-4-solutions-to-generate-consecutive-sequence)
- [3103. Find Trending Hashtags II](https://leetcode.com/problems/find-trending-hashtags-ii/description/)
- Generate a sequence of integers from 1 to 100
  - Notice that `< 100`, not `<= 100`

```
with recursive cte as
(
  select 1 as value
  union all
  select value + 1
  from cte
  where value < 100
)

select *
from cte
;
```

Recursive CTE can also decrement. The below stops when subtask_id is 2, so 2 - 1 = 1, and actual final subtask_id is 1.

```sql
with recursive
cte as (
  select
    task_id,
    subtasks_count as subtask_id
  from
    tasks
  union all
  select
    task_id,
    subtask_id - 1 as subtask_id
  from
    cte
  where
    subtask_id > 1
)
```

A recursive CTE consists of a nonrecursive `SELECT` part followed by a recursive `SELECT` part.

## ROW_NUMBER()

- Assign a sequential number to each row.
- [MySQL ROW_NUMBER Function](https://www.mysqltutorial.org/mysql-window-functions/mysql-row_number-function/)
- If you want to make a tie in partition order by, use `RANK()` instead of `ROW_NUMBER()`
  - [How to include a row number but show a tie?](https://stackoverflow.com/questions/9561171/how-to-include-a-row-number-but-show-a-tie)

## Over Clause

- [What Is the MySQL OVER Clause?](https://learnsql.com/blog/over-clause-mysql/)

## Lead()

- [1709. Biggest Window Between Visits](https://leetcode.com/problems/biggest-window-between-visits/)

## MIN() vs LEAST()

- `MIN()` is typically used to return the minimum value in a column in a database. The table could contain many rows, but this function returns the one with the minimum value.
- `LEAST()` on the other hand, returns the minimum-valued argument from the list of arguments passed to it. So you could pass say, 3 arguments to this function and it will return the one with the smallest value.
- [MIN() vs LEAST() in MySQL: What’s the Difference?](https://database.guide/min-vs-least-in-mysql-whats-the-difference/)
- Work in PostgreSQL too.

## GREATEST

- Use `GREATEST(col1, col2, ...)` to get a max from multiple columns.
- [2783. Flight Occupancy and Waitlist Analysis](https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/description/)
- Work in PostgreSQL too.

## Median

- [569. Median Employee Salary](https://leetcode.com/problems/median-employee-salary/)
- [571. Find Median Given Frequency of Numbers](https://leetcode.com/problems/find-median-given-frequency-of-numbers/)

## UNION vs UNION ALL

- `UNION` removes duplicate records, but `UNION ALL` doesn't.
- [What is the difference between UNION and UNION ALL?](https://stackoverflow.com/questions/49925/what-is-the-difference-between-union-and-union-all)
- Comments in [Follow up solution ](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/discuss/146577/Follow-up-solution)

## Day of week

- `DAYOFWEEK(date)` returns 1 (Sunday), 2 (Monday), ... 7 (Saturday)
- `WEEKDAY(date)` returns 0 (Monday), 1 (Tuesday), ... 6 (Sunday)
  - I think this is more useful because it's easy to separate weekend and not-weekend by `< 5` or not.

## REGEXP

- `REGEXP` performs regular expression pattern matches.
- `^ab` means starts with 'ab' like 'abc', not 'acc'
- Use two backslashes `\\` to use literal instance of special characters.
  - To match '-', `\\-`
- `abc$` means ends with 'abc'
- `*` means 0 or more instances of string preceding it. `a*` is 'a', 'aa', or ''.
- [MySQL | Regular expressions (Regexp)](https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/)
- [12.8.2 Regular Expressions](https://dev.mysql.com/doc/refman/8.0/en/regexp.html)
- [3103. Find Trending Hashtags II ](https://leetcode.com/problems/find-trending-hashtags-ii/description/)
- `REGEXP_SUBSTR(string_column, pattern_string)` to extract expression from a string column
  - `regexp_substr(tweet, '#[a-zA-Z]+')` extracts hashtag from a tweet.
- `REGEXP_REPLACE(string_column, pattern_string, 1based_start_index, num_occurrence)` to replace.
  - `regexp_replace(tweet, '#[a-zA-Z]+', '', 1, 1)` removes one leftmost tag from a tweet if it contains multiple tags.


## TRIM

- `TRIM(string)` removes leading and trailing whitespaces
- [How to remove leading and trailing whitespace in a MySQL field?](https://stackoverflow.com/questions/6858143/how-to-remove-leading-and-trailing-whitespace-in-a-mysql-field)

## LOWER

- `LOWER(string)` converts all the characters in a string to lowercase characters.

## LENGTH()

- `LENGTH(string)` returns a number of characters
  - e.g. `WHERE LENGTH(string_column) > 15`

## TIMESTAMPDIFF()

- `TIMESTAMPDIFF(unit, earlier_date, later_date)` returns time difference in the `unit`
  - e.g. `where timestampdiff(second, timestamp1, timestamp2) <= 60 * 60 * 24` checks if two timestamps are within 24 
    hours window.
  - Difference in minute `timestampdiff(minute, start_datetime, end_datetime)`
- Unlike BigQuery SQL, this function can be applied to `DATETIME` columns, even if the function name says timestamp.
- [1939. Users That Actively Request Confirmation Messages](https://leetcode.com/problems/users-that-actively-request-confirmation-messages/)
- [Average Commute Time](https://www.interviewquery.com/questions/average-commute-time)
- [MySQL TIMESTAMPDIFF() function](https://www.w3resource.com/mysql/date-and-time-functions/mysql-timestampdiff-function.php)

## Cumulative sum

- `SUM(amount_to_be_cumsummed) OVER(PARTITION BY group ORDER BY order_reference_of_cumsum)`
- [2004. The Number of Seniors and Juniors to Join the Company](https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/)
- [534. Game Play Analysis III](https://leetcode.com/problems/game-play-analysis-iii/)
- [2066. Account Balance](https://leetcode.com/problems/account-balance/)
- [1204. Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/)

## CAST(_ as SIGNED)

- [2175. The Change in Global Rankings](https://leetcode.com/problems/the-change-in-global-rankings/)
- [11.1.7 Out-of-Range and Overflow Handling](https://dev.mysql.com/doc/refman/8.0/en/out-of-range-and-overflow.html)
- [When should I use UNSIGNED and SIGNED INT in MySQL?](https://stackoverflow.com/questions/11515594/when-should-i-use-unsigned-and-signed-int-in-mysql)
- [12.11 Cast Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html)

## CREATE FUNCTION

- [2205. The Number of Users That Are Eligible for Discount](https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/)
- [MySQL | Creating stored function](https://www.geeksforgeeks.org/mysql-creating-stored-function/)

## CREATE PROCEDURE

- Need `;` before `END`
- [2230. The Users That Are Eligible for Discount](https://leetcode.com/problems/the-users-that-are-eligible-for-discount/)

```sql
CREATE PROCEDURE name(args TYPE)
BEGIN
  regular SQL code
  ;
END
```

## LAG

- [MySQL LAG Function](https://www.mysqltutorial.org/mysql-window-functions/mysql-lag-function/)

## SET

A user-defined variable is written as `@var_name` abd assigned an value as follows

`SET @var_name = expression;`

## SELECT INTO variable

- [2252. Dynamic Pivoting of a Table](https://leetcode.com/problems/dynamic-pivoting-of-a-table/)
- [MySQL SELECT INTO Variable](https://www.mysqltutorial.org/mysql-select-into-variable/)

## Prepared statement

- [MySQL Prepared Statement](MySQL Prepared Statement)
- [2252. Dynamic Pivoting of a Table](https://leetcode.com/problems/dynamic-pivoting-of-a-table/)

## INFORMATION_SCHEMA

`INFORMATION_SCHEMA` is a database. It's visible as a normal database. It contains information about other databases.
It's available in every MySQL instance and store metadata. It's called the system catalog or data dictionary.

- [2253. Dynamic Unpivoting of a Table](https://leetcode.com/problems/dynamic-unpivoting-of-a-table/)

## FIRST_VALUE

- Repeat the value in the first row to the subsequent rows
- Below, the first value in `col1` within a group by `col2` will be repeated within groups.

```sql
FIRST_VALUE(col1) OVER(PARTITION BY col2)
```

- [2388. Change Null Values in a Table to the Previous Value](https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/)
- [MySQL FIRST_VALUE Function](https://www.mysqltutorial.org/mysql-window-functions/mysql-first_value-function/)

## TIMESTAMPDIFF()

- `TIMESTAMPDIFF(unit, start, end)`. Unit could be `second`, `minute` etc.

## CEILING()

- To round up

## IFNULL()

- `ifnull()` can be used in `WHERE` clause when `null` occurs by joining tables.

## BETWEEN

- `BETWEEN value1 and value2` where `value1` < `value2`.
- e.g. `BETWEEN '2018-06-23' AND '2019-06-23'`
- [1747. Leetflex Banned Accounts](https://leetcode.com/problems/leetflex-banned-accounts/)

## CROSS JOIN

When we want to get all the combinations of records, we can either `CROSS JOIN` or multiple tables in `FROM`.

`FROM t1 CROSS JOIN t2` or `FROM t1, t2`

But if you wanna join the resulted table to another table, only `CROSS JOIN` works.

`FROM t1 CROSS JOIN t2 LEFT JOIN t3 ON t1.a = t3a` works.

But `FROM t1, t2 LEFT JOIN t3 ON t1.a = t3.a` doesn't work.

- [1990. Count the Number of Experiments](https://leetcode.com/problems/count-the-number-of-experiments/)
- [It is the worst question! (2 Solutions, dynamic without using UNION hard code)](https://leetcode.com/problems/count-the-number-of-experiments/discuss/1445116/It-is-the-worst-question!-(2-Solutions-dynamic-without-using-UNION-hard-code))

## ROWS BETWEEN AND in OVER()

- Basic syntax is `ROWS BETWEEN lower_bound AND upper_bound` in `OVER(PARTITION BY _ ORDER BY _ ROWS BETWEEN _ AND _)`
- The bounds have several forms.
- `OVER(PARTIION BY _ ORDER BY _ ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING)`
  - Checks the rows between all the rows before the current row and the 1 row before the current row
- [5 Practical Examples of Using ROWS BETWEEN in SQL](https://learnsql.com/blog/sql-window-functions-rows-clause/)

## Pivot

- [618. Students Report By Geography](https://leetcode.com/problems/students-report-by-geography/description/)

## DATE_ADD

`DATE_ADD(date_column, INTERVAL number unit)`

e.g. `ON date = DATE_ADD(date, INTERVAL 1 DAY)`

## DATE_SUB

- Subtract a specified unit like day from a date
- e.g. Subtract 1 day from a date column `DATE_SUB(date_column, INTERVAL 1 DAY)`
- Official solution of [1097. Game Play Analysis V](https://leetcode.com/problems/game-play-analysis-v/description/)

## Group ID by taking difference from ROW_NUMBER()

- [1225. Report Contiguous Dates](https://leetcode.com/problems/report-contiguous-dates/description/)

## COUNT() OVER()

- `COUNT` can work as window function
- argument needs to be supplied in `COUNT()`
- `COUNT(column_name_1) over(partition by column_name_2)`
- [1369. Get the Second Most Recent Activity](https://leetcode.com/problems/get-the-second-most-recent-activity/description/)

## ORDER BY RAND() to select random records

- [MySQL Select Random Records](https://www.mysqltutorial.org/select-random-records-database-table.aspx)
- [Interview Query, Uniform Car Maker](https://www.interviewquery.com/questions/uniform-car-maker)

## Pivot a table in SQL

- [Exam Scores](https://www.interviewquery.com/questions/exam-scores)
- Use `sum(case when ... then ... else ... end) ... group by`

## FLOOR()

- Largest integer that is smaller than or equal to a number
  - `FLOOR(1.1)` is `1`
  - `FLOOR(-1.1)` is `-2`, not `-1` because `-2` is smaller than `-1.1`
- [Average Commute Time](https://www.interviewquery.com/questions/average-commute-time)

## VAR_SAMP()

- `VAR_SAMP()` computes `sample variance`.
- Sample variance uses `n - 1` to divide the sum of the differences between `sample mean` and each data.
- [t Value via SQL](https://www.interviewquery.com/questions/t-value-sql)
- [Population variance and sample variance](https://en.wikipedia.org/wiki/Variance#Population_variance_and_sample_variance)
- [VAR_SAMP() function in MySQL](https://www.geeksforgeeks.org/var_samp-function-in-mysql/)

## WEEK()

`WEEK(date_column)` returns the week number for a given date from 0 to 53. This function can be used to identify which 
nth week a date belongs to.

- [2993. Friday Purchases I](https://leetcode.com/problems/friday-purchases-i/description/)

## Hard-code data as string and convert to data

`SELECT DATE '2024-04-05' as date_column;`, `DATE` is a type keyword placed in front of string to make it date.

https://dev.mysql.com/doc/refman/8.3/en/date-and-time-literals.html#date-and-time-standard-sql-literals