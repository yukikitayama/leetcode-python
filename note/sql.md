# SQL

- Filter records which have missing
  - `WHERE column_name IS NULL`
- If a value in a column is null, replace with something
  - `IFNULL(column_name, 0)` e.g. Replace with 0 if it's missing