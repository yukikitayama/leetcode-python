# Amortized analysis

It gives the **average performance** over time of each operation in the **worst** case.

The worst case operation can **alter the state** in such a way that the **worst case cannot occur again for a long time**.

For example, a particular operation takes `O(n)` once and other times it takes `O(1)`. If we run this operation `n` times, the 
worst case seems to be `O(n^2)` but we say `O(1)` average time per operation.

## LeetCode example

- https://leetcode.com/problems/implement-queue-using-stacks/description/
