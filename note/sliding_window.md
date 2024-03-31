# Sliding window

The problems that sliding window can solve have the following properties
1. If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid.
2. If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid.

Sliding window is applicable when the problem entails achieving a goal using **subarrays**, and the **individual 
elements cannot be independently selected**.

https://leetcode.com/problems/subarray-sum-equals-k/solutions/301242/general-summary-of-what-kind-of-problem-can-cannot-solved-by-two-pointers/

## Math

- Incrementing `ans` by `right - left + 1` every time when `right` iterates is a typical math with sliding window.
  - https://leetcode.com/problems/subarrays-with-k-different-integers/

## Problems that sliding window can solve

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

## Problems that sliding window cannot solve

When `k = 3`, `1, 1, 1` sum is `3`, but `1, 1` sum is `2`. Wider is valid, but narrower is invalid. It violates the 
property 1.

When `k = 2`, `1, 1, 1` sum is `3`, but `1, 1, -1, 1` sum is `2`. Narrower is invalid, but wider is valid. It violates 
the property 2.

So this problem cannot use sliding window.

## Problem that does not use left pointer

- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters)
  - This approach optimize space
  - Expand but doesn't contract, but keep sliding

## Prefix product

`right - left + 1` magic to compute count

https://leetcode.com/problems/subarray-product-less-than-k/

