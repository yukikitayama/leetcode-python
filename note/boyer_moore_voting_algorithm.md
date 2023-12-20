# Boyer-Moor Voting Algorithm

Algorithm to find an item in a list with linear time and **constant space**.

Given an array of integers, `n` is the length of the array,
- There can be at most **one** majority element which is more than `n / 2` times
  - `[1, 1, 1, 2]`
- There can be at most **two** majority elements which are more than `n / 3` times
  - `[1, 1, 1, 1, 2, 3, 3, 3, 3]`
- There can be at most **three** majority elements which are more than `n / 4` times
and so on.


- There can be at most **one** majority element which is more than `n / 2` times

While scanning the array, the counter is incremented if you encounter an element which is exactly same as the potential candidate but decremented otherwise. When the counter reaches zero, the element which will be encountered next will become the potential candidate. Keep doing this procedure while scanning the array. However, when you have exhausted the array, you have to make sure that the element recorded in the potential candidate variable is the majority element by checking whether it occurs more than ⌊n/2⌋ times in the array.
If an element is truly a majority element, it will stick in the potential candidate variable, no matter how it shows up in the array (i.e. all clustered in the beginning of the array, all clustered near the end of the array, or showing up anywhere in the array), after the whole array has been scanned. Of course, while you are scanning the array, the element might be replaced by another element in the process, but the true majority element will definitely remain as the potential candidate in the end.

## LeetCode

- [169. Majority Element
](https://leetcode.com/problems/majority-element/)
- [229. Majority Element II
](https://leetcode.com/problems/majority-element-ii/description/)