"""
nums1[i] + nums1[j] > nums2[i] + nums2[j]
i < j

2 + 2 > 1 + 1

nums1[i] - nums2[i] > nums2[j] - nums1[j]
2 - 1 > 1 - 2
1 > -1

nums1[i] - nums2[i] - nums2[j] + nums1[j] > 0
(nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
"""

from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = []
        for i in range(len(nums1)):
            diff.append(nums1[i] - nums2[i])
        diff.sort()

        ans = 0

        left = 0
        right = len(nums1) - 1
        while left < right:
            if diff[left] + diff[right] > 0:
                # right: 3, left: 1, we have 2 pairs
                # because, by fixing right, increment left, always gives us a large diff sum
                # because diff array is sorted, so if curr right plus curr left is greater than 0
                # curr right plus (left + 1) is also greater than 0
                ans += right - left
                right -= 1
            else:
                left += 1

        return ans
