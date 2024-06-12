# Binary Search

- Whenever working with sorted array, it's always worth considering whether binary search can be applied to the problem.
- To test whether your binary search correctly will terminate, test an input of size 2 and check if it reduces the search
  space to a single element.

## Concept

- `Search space`
  - A contiguous sequence with a specified left and right index that Binary Search operates on.
- An algorithm that divides the search space in two spaces after every comparison.
- `left`, `mid`, `right`
  - Index pointers necessary in binary search
- `Post-processing`
  - Binary search is implemented to use the while loop
  - Post-processing is lines of codes that needs to be done after the while loop terminates.
- **Upper bound** is the **rightmost** possible position to insert.
  - When there are duplicated numbers which are the same as the number to insert, the number will be inserted after them
- **Lower bound** is the **leftmost** possible position to insert.
  - When there are duplicated numbers which are the same as the number to insert, the number will be inserted before them

## Implementation

- Binary Search can take many alternate forms.
- People say that 99% of the binary search problems fall into one of the following 3 ways to implement it.
- The three implementations differ in index assignment, the while loop termination condition, and post-processing.
- https://medium.com/swlh/binary-search-find-upper-and-lower-bound-3f07867d81fb

### While loop left <= right

- The while loop ends when there is no element left in search space
- So after the while loop ends, `left` and `right` pointers are not usable.
- And nothing needs to be done after the loop, so it's only able to return `-1` for example.

### While loop left < right

- Use `right` to determine if the condition is met and decide whether to go left or right
- Guarantees search space always has at least `2` elements at each step
- The while loop ends when there is `1` element left in search space

### While loop left + 1 < right

- Use `left` and `right` to determine if the condition is met and decide whether to go left or right
- Guarantees search space always has at least `3` elements at each step
- The while loop ends when there is `2` elements left in search space

## Complexity

- Time is `O(logN)`, because `N` gets half every time.
- Space is `O(1)`, because it only uses 3 pointers, `left`, `mid`, and `right`.

## LeetCode

- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
  - It's not obvious from the problem statement to notice that this is a binary search problem.
- [1891. Cutting Ribbons](https://leetcode.com/problems/cutting-ribbons/)
  - This is also not obvious from the problem that it's a binary search question.
  - https://medium.com/swlh/binary-search-find-upper-and-lower-bound-3f07867d81fb
  - https://leetcode.com/problems/cutting-ribbons/submissions/1177253885/
  - https://leetcode.com/problems/cutting-ribbons/solutions/2575525/python-concise-code-binary-search/
- Boundary search
  - [2141. Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/description/)

## Math

`mid = (left + right) // 2`, when the range is odd, middle one is picked. When the range is even, the left one in the 2 centers is picked.

`mid = left + (right - left) // 2`, when the range is odd, middle one is picked. When the range is even, the left one in the 2 centers is picked.

`mid = left + (right - left + 1) // 2`, when the range is odd, middle one is picked. When the range is even, the right one in the 2 centers is picked.

So conceptually, `(left + right) // 2` and `left + (right - left) // 2` are the same.

## Template

Most basic and elementary form of Binary Search.
- Initial Condition: left = 0, right = length-1
- Termination: left > right
- Searching Left: right = mid-1
- Searching Right: left = mid+1

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# End Condition: left > right
return -1
```
