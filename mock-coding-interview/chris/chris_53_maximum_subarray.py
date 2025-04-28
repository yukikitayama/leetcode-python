"""
Prefix sum
nums:      [-2,  1, -3, 4, -1, 2, 1, -5, 4]
Prefix: [0, -2, -1, -4, 0, -1, 1, 2, -3, 1]

Sliding window
Kadane's algo
  max so far (ans)
  keep current prefix sum
  if it becomes negative
    running prefix sum reset to 0
nums:      [-2,  1, -3, 4, -1, 2, 1, -5, 4]
  -2,
  1
  1 - 3 = -2
  4
  4 - 1 = 3 (ans)
  3 + 2 = 5 (ans),
  5 + 1 = 6 (ans)
  6 - 5 = 1
  1 + 4 = 5

nums: [-3, -2, -1]
  ans: -inf
  -3 (ans)
  -2 (ans)
  -1 (ans)

nums: [5,4,-1,7,8]
  ans: -inf
  prefix: 0
  5 (ans)
  5 + 4 =  9(ams)
  9 - 1 = 8
  8 + 7 = 15 (ans)
  15 + 8 = 23 (ans)

[-2,  1, -3, 4, -1, 2, 1, -5, 4]
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            ans = max(ans, prefix_sum)

            if prefix_sum < 0:
                prefix_sum = 0

        return ans


