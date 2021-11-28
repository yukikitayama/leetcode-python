from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi

        return lo


"""
Time complexity
O(logN)
Space complexity
O(1)
"""
