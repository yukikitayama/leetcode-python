"""
100,000,000

[5,-3,5] + [5,-3,5]
Keep window side at most N
[5, 2, 7, 12, 9, 14]

[5, -3, 5, 5, -3, 5]
  5
  5 - 3 = 2
  2 + 5 = 7
  7 + 5 = 12

Kadane's algo N times
  O(N^2)

nums: [5, -3, 5]
  max: 7
  min: -3
  max - min = 10

nums: [1, -2, 3, -2]
  first K: 3
  second K: total: 0, min: -2, 2, [3, -2, 1]

First kadane's
Second min kadane's
If first kanane - second kadane > first,
  use the comb
Else
  use only first

First, do usual kadane's to find max subarray
Second, get sum of array, and do min kadane's to find min subarray
  total - min subarray = biggest remaining
Return bigger of first or second

[-3, -2, -3]
min: -8
total: -8
total - min = 0

https://leetcode.com/problems/maximum-sum-circular-subarray/description/
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        first_k = float("-inf")
        prefix = 0
        for num in nums:
            prefix += num
            first_k = max(first_k, prefix)
            if prefix < 0:
                prefix = 0

        second_k = float("inf")
        prefix = 0
        for num in nums:
            prefix += num
            second_k = min(second_k, prefix)
            if prefix > 0:
                prefix = 0

        total = sum(nums)

        # print(first_k, total, second_k)

        if total - second_k == 0:
            return first_k
        else:
            return max(first_k, total - second_k)

