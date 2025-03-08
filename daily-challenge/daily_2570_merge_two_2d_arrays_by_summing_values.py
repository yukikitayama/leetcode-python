"""
Two pointers
if Current IDs are the same
  sum
  increment both pointers
if p1 num is smaller
  p1 append to ans
  increment p1
if p2 num is smaller
  p2 append
  increment p2
When one of the arrays finish earlier
  append the rest of the other array to ans
"""

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):

            if nums1[p1][0] == nums2[p2][0]:
                sum_ = nums1[p1][1] + nums2[p2][1]
                ans.append([nums1[p1][0], sum_])
                p1 += 1
                p2 += 1

            elif nums1[p1][0] < nums2[p2][0]:
                ans.append(nums1[p1])
                p1 += 1

            elif nums1[p1][0] > nums2[p2][0]:
                ans.append(nums2[p2])
                p2 += 1

        while p1 < len(nums1):
            ans.append(nums1[p1])
            p1 += 1

        while p2 < len(nums2):
            ans.append(nums2[p2])
            p2 += 1

        return ans