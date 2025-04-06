# Amortized analysis

- It gives the **average performance** over time of each operation in the **worst** case.
- The worst case operation can **alter the state** in such a way that the **worst case cannot occur again for a long time**.
- For example, a particular operation takes `O(n)` once and other times it takes `O(1)`. If we run this operation `n` times, the 
worst case seems to be `O(n^2)` but we say `O(1)` average time per operation.
- If you average out the time it takes for a function to run across `n` calls, it works out to be `O(1)`.

## LeetCode example

- https://leetcode.com/problems/implement-queue-using-stacks/description/
- [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/description/)
- [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/editorial/)
- [1429. First Unique Number](https://leetcode.com/problems/first-unique-number/description/)
