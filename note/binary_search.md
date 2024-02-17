# Binary Search

- Whenever working with sorted array, it's always worth considering whether binary search can be applied to the problem.

## Concept

- `Search space`
  - A contiguous sequence with a specified left and right index that Binary Search operates on.
- An algorithm that divides the search space in two spaces after every comparison.
- `left`, `mid`, `right`
  - Index pointers necessary in binary search
- `Post-processing`
  - Binary search is implemented to use the while loop
  - Post-processing is lines of codes that needs to be done after the while loop terminates.

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