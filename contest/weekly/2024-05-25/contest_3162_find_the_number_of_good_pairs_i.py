"""
Brute force
"""

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0

        for n in range(len(nums1)):
            for m in range(len(nums2)):
                if nums1[n] % (nums2[m] * k) == 0:
                    ans += 1

        return ans