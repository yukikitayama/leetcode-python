"""
nums: [1, 2]
subarray: [1], [2], [1, 2]
nums: [1, 2, 3]
subarray: [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]
  X: [1, 3]

Brute force
  nested for loop
    if the current subaray size divisible by k
      get max of ans and current sum
T: O(N**2 * N)
S: O(1)

Prefix sum
k: 4
nums: [-1,-2,-3,-4,-5]
prefix sum: [0, -1, -3, -6, -10, -15]
  subarray: [-1,-2,-3,-4]
  subarray sum = prefix[4 = right] - prefix[0 = left] = -10 - 0 = -10
    (right - left) % k = (4 - 0) % 4 = 4 % 4 = 0
  subarray: [-2,-3,-4,-5] = -14
  subaaray sum = prefix[5] - prefix[1] = -15 - (-1) = -14
    (right - left) % k = (5 - 1) % 4 = 4 % 4 = 0
(right - left) % k should be 0
  this is the array to compute sum
Efficiently get two pointers
Sliding window
  nums: [-1,-2,-3,-4,-5], k: 2
  left: 0, right: 2,
  left: 1, right: 3
  left: 1, right: 4
    Recall, there was left: 0
    left: 0, right: 4
Hashmap
  k: index
  v: prefix sum from 0 to i
Iterate from left to right
  iterate all the keys in hashmap
    if (current index - key) % k == 0:
      get sum
  each time record current index and prefix sum to hashmap
T: O(N**2)
S: O(N)

index % k
  k: 4
  0 % 4 = 0,
  1 % 4 = 1
  ...
  4 % 4 = 0
"""

from typing import List
import itertools


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [float("inf")] * k
        prefix[-1] = 0

        ans = float("-inf")

        for i, pre in enumerate(itertools.accumulate(nums)):
            ans = max(ans, pre - prefix[i % k])
            prefix[i % k] = min(prefix[i % k], pre)

        return ans