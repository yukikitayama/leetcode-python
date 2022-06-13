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

## GROUP_CONCAT()

- Concatenate string from a group into a single string with options such as separator.
- e.g. `GROUP_CONCAT(DISTINCT col ORDER BY col separator ',')`
  - `seperator ','` can be omitted because by default ',' is a separator.
- [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/)
- [MySQL GROUP_CONCAT Function](https://www.mysqltutorial.org/mysql-group_concat/)
  
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

- `DATE_FORMAT(DATE, 'FORMAT_STRING')`
- `%m`: month `00` to `12`
- `%Y`: 4 digits year
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

## Recursive Common Table Expression

- A common table expression using `with recursive` and having a subquery inside referring to its own table
- [1613. Find the Missing IDs](https://leetcode.com/problems/find-the-missing-ids/)
- [Recursive Common Table Expressions](https://dev.mysql.com/doc/refman/8.0/en/with.html#common-table-expressions-recursive)
- [Generate an integer sequence in MySQL](https://stackoverflow.com/questions/304461/generate-an-integer-sequence-in-mysql)
- [[MySQL] 4 solutions to generate consecutive sequence](https://leetcode.com/problems/find-the-missing-ids/discuss/890608/MySQL-4-solutions-to-generate-consecutive-sequence)
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

## ROW_NUMBER()

- Assign a sequential number to each row.
- [MySQL ROW_NUMBER Function](https://www.mysqltutorial.org/mysql-window-functions/mysql-row_number-function/)

## Over Clause

- [What Is the MySQL OVER Clause?](https://learnsql.com/blog/over-clause-mysql/)

## Lead()

- [1709. Biggest Window Between Visits](https://leetcode.com/problems/biggest-window-between-visits/)

## MIN() vs LEAST()

- `MIN()` is typically used to return the minimum value in a column in a database. The table could contain many rows, but this function returns the one with the minimum value.
- `LEAST()` on the other hand, returns the minimum-valued argument from the list of arguments passed to it. So you could pass say, 3 arguments to this function and it will return the one with the smallest value.
- [MIN() vs LEAST() in MySQL: What’s the Difference?](https://database.guide/min-vs-least-in-mysql-whats-the-difference/)

## Median

- [569. Median Employee Salary](https://leetcode.com/problems/median-employee-salary/)
- [571. Find Median Given Frequency of Numbers](https://leetcode.com/problems/find-median-given-frequency-of-numbers/)

## UNION vs UNION ALL

- `UNION` removes duplicate records, but `UNION ALL` doesn't.
- [What is the difference between UNION and UNION ALL?](https://stackoverflow.com/questions/49925/what-is-the-difference-between-union-and-union-all)

## Day of week

- `DAYOFWEEK(date)` returns 1 (Sunday), 2 (Monday), ... 7 (Saturday)
- `WEEKDAY(date)` returns 0 (Monday), 1 (Tuesday), ... 6 (Sunday)

## REGEXP

- `REGEXP` performs regular expression pattern matches.
- `^ab` means starts with 'ab' like 'abc', not 'acc'
- Use two backslashes `\\` to use literal instance of special characters.
  - To match '-', `\\-`
- `abc$` means ends with 'abc'
- `*` means 0 or more instances of string preceding it. `a*` is 'a', 'aa', or ''.
- [MySQL | Regular expressions (Regexp)](https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/)
- [12.8.2 Regular Expressions](https://dev.mysql.com/doc/refman/8.0/en/regexp.html)
