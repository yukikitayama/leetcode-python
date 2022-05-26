/*
Generate number sequence for each num, and combine all together, and row_number(), and find median

num freq    left    right   abs_diff
0   7       7       12      5
1   1       8       5       3
2   3       11      4       7
3   1       12      1       11

if difference between left and right is less or equal to frequency of the current number,
the current number is median
*/

select
  avg(a.num) as median
from
  numbers as a
where
  a.frequency >= abs(
    (
      select  sum(frequency) from numbers where
        num <= a.num
    )

    -

    (
      select  sum(frequency) from numbers where
        num >= a.num
    )
  )
;

