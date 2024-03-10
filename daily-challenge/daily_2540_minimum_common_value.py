from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # Longer array will be search space of binary search
        if len(nums1) > len(nums2):
            self.getCommon(nums2, nums1)

        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1

            # Terminate: left = right + 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return True

            return False

        for num in nums1:
            if binary_search(nums2, num):
                return num

        return -1

    def getCommon1(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]

            elif nums1[p1] < nums2[p2]:
                p1 += 1

            elif nums1[p1] > nums2[p2]:
                p2 += 1

        return -1