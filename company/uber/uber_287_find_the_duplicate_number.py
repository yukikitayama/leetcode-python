"""
- 2d (tortoise) = d (hare)
= 2(F + a) = F + a + nC
  F + a = nC, is the intersection
  - F is the distance from the start to the entrance of cycle
  - a is the distance that tortoise walked from the entrance up to some point in cycle
  - C is cycle
  - Before hare meets tortoise the intersection, hare cycled n times
  -
"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare






