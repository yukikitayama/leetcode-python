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
- Concatenate string from a group into a single string with options such as separator.
  - `GROUP_CONCAT()`
    - e.g. `GROUP_CONCAT(DISTINCT col ORDER BY col separator ',')`
  - [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/)