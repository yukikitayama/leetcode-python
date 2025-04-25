"""
hashmap k: num2, v: array of num2 indices
"""

from typing import List
import collections


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_to_indices = collections.defaultdict(list)
        for i, num2 in enumerate(nums2):
            num2_to_indices[num2].append(i)

        ans = []

        for num1 in nums1:
            i = num2_to_indices[num1].pop()
            ans.append(i)

        return ans
