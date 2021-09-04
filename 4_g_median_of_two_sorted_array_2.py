from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)

        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x

        while low <= high:
            partition_x = int((low + high) / 2)
            partition_y = int((x + y + 1) // 2) - partition_x
