"""
Make two hashset
num1 counter 0
num2 counter 0
iterate nums1 and num2
  id nums1 num appear at nums hashset increment
  do similarly for nums
"""

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = 0
        counter2 = 0
        hashset1 = set(nums1)
        hashset2 = set(nums2)

        for i in range(len(nums1)):
            if nums1[i] in hashset2:
                counter1 += 1

        for i in range(len(nums2)):
            if nums2[i] in hashset1:
                counter2 += 1

        return [counter1, counter2]