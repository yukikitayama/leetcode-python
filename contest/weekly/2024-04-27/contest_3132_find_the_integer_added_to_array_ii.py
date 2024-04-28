"""
Binary search?

nums1 = [4,20,16,12,8], nums2 = [14,18,10]
[4, 8, 12, 16, 20]
[10, 14, 18]

Naive
  Remove 2 elements from nums1
  sort nums1 and nums2
  iterate two arrays
    if difference isn't constant
      The removed 2 elements were not good
  If iteration was successful
    record difference and keep minimum difference

[4,6,3,1,4,2,10,9,5]
[5,10,3,2,6,1,9]
exp: 0
"""

from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        ans = float("inf")

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                diff = None
                p1 = 0
                p2 = 0
                constant = True
                while p1 < len(nums1) and p2 < len(nums2):
                    while p1 in [i, j]:
                        p1 += 1
                    if diff is None:
                        diff = nums2[p2] - nums1[p1]
                    elif nums2[p2] - nums1[p1] != diff:
                        constant = False
                    elif nums2[p2] - nums1[p1] == diff:
                        pass

                    p1 += 1
                    p2 += 1

                if constant:
                    ans = min(ans, diff)

        return ans
