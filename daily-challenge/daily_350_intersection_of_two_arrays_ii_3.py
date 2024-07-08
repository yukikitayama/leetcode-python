from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)

        for k in c1.keys():

            if k in c2:
                for _ in range(min(c1[k], c2[k])):
                    ans.append(k)

        return ans