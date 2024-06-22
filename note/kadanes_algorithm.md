# Kadane's Algorithm

**Kadane's algorithm** is a DP algorithm to find the maximum subarray sum in an array of integers which could include negative values. 
Algorithm traverses from left to right. It efficient because T: O(N) and S: O(1).
It maintains 2 values
- Global max: Maximum sum encountered so far
- Local max: Maximum sum ending at the current index

https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
- [2272. Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/description/)
  - Hard
