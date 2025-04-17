"""
e.g.
  k: 4, num: 2, 2 / 4 =

Hashmap
  k: num
  v: count
iterarte from left to right
  if current element squared is divisible by k and current element in hashmap
    increment ans by the value in hashmap
"""

from typing import List
import collections


class Solution:

    def countPairs(self, nums: List[int], k: int) -> int:

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1
        return ans

    def countPairs1(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        ans = 0

        for num in nums:

            if num in counter and (num ** 2) % k == 0:
                ans += counter[num]

            counter[num] += 1

        return ans