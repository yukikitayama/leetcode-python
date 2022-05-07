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