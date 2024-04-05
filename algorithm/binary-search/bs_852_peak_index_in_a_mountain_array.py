"""
binary search
  if mid num bigger than left and right
    found target
  if left num is bigger
    search to left
  if right num is bigger
    search to right
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """Find single element search space style binary search"""
        left = 0
        right = len(arr) - 1
        # Break when search space becomes single element
        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                # left doesn't include mid because mid won't be peak
                left = mid + 1

            else:
                # We don't know if mid is peak yet, but at least mid is bigger than right next
                # so keep mid in the search space
                right = mid

        # Here search space is reduce to single element
        # so either left or right pointer can work
        return left

    def peakIndexInMountainArray1(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid != 0 and mid != len(arr) - 1 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            elif mid != 0 and arr[mid - 1] > arr[mid]:
                right = mid - 1
            elif mid == 0:
                left = mid + 1

            elif mid != len(arr) - 1 and arr[mid + 1] > arr[mid]:
                left = mid + 1
            elif mid == len(arr) - 1:
                right = mid - 1
