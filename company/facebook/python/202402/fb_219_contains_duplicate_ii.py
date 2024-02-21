"""
two pointer sliding window
contract when window > k
as soon as find the indices return True
otherwise return false

hashmap
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashset = set()

        for i in range(len(nums)):

            curr = nums[i]

            if curr in hashset:
                return True

            hashset.add(curr)

            if len(hashset) > k:
                hashset.discard(nums[i - k])

        return False