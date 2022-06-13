-- ^ matches the beginning of the string
-- [A-Z] matches any upper case letters
-- [a-z] matches any lower case letters
-- ^[A-Za-z] means starts with letters
-- \\ means use literal string of special characters
-- `$` means ends with preceiding characters
-- * means use 0 or more string of preceiding characters
select
  *
from
  users
where
  mail regexp '^[A-Za-z][A-Za-z0-9\\_\\.\\-]*@leetcode\\.com$'
;
