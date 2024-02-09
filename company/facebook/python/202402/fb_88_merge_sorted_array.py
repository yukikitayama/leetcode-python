"""
Three pointers
  pointer starts from m - 1 and n - 1
  insert pointer starts from nums1 length - 1
Iterate from right
  by m and n pointer, bigger element insert by insert pointer
  decrement pointers

Break loop when either m or n pointer < 0

remaining pointer

eg
  [5, 6, 7, 0, 0, 0], [1, 2, 3]
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        p_insert = m + n - 1

        for p_insert in range(m + n - 1, -1, -1):
            # If finish moved p2 element, it means that all p2 elements were bigger than p1
            # and given p1 elements are already sorted so nothing to be done
            if p2 < 0:
                break

            # If p1 is still remaning and if need move p1
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_insert] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_insert] = nums2[p2]
                p2 -= 1

        print(nums1)
