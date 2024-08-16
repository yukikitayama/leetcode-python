# Permutation

3 types of permutation questions
- Generate all permutations
  - Backtracking
- Generate next permutation
  - D.E. Knuth algorithm
- Generate k-th permutation
  - Factorial number system

**D.E. Knuth algorithm** generates a new permutation from the previous one on O(N) time to generate permutations in lexicographically sorted order.

There is a much more permutations than subsets.

**N! grows up much faster than 2^N**.

The solution space provided by the positional system with a constant base cannot match with the number of permutations (?)

**Factorial number system** is a positional systems with **non-constant base m!**.

https://en.wikipedia.org/wiki/Factorial_number_system

## LeetCode

- [46. Permutations](https://leetcode.com/problems/permutations/description/)
  - Generate all permutations
- [31. Next Permutation](https://leetcode.com/problems/next-permutation/description/)
  - Generate next permutation
- [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/description/)
  - Generate k-th permutation
  - Use **factorial number system**