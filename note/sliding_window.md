# Sliding window

The problems that sliding window can solve have the following properties
1. If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid.
2. If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid.

https://leetcode.com/problems/subarray-sum-equals-k/solutions/301242/general-summary-of-what-kind-of-problem-can-cannot-solved-by-two-pointers/

## Problems that sliding window can solve

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

## Problems that sliding window cannot solve

https://leetcode.com/problems/subarray-sum-equals-k/description/

When `k = 3`, `1, 1, 1` sum is `3`, but `1, 1` sum is `2`. Wider is valid, but narrower is invalid. It violates the 
property 1.

When `k = 2`, `1, 1, 1` sum is `3`, but `1, 1, -1, 1` sum is `2`. Narrower is invalid, but wider is valid. It violates 
the property 2.

So this problem cannot use sliding window.

