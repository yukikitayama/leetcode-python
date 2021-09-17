from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1

        return nums1[:k]


"""
Time complexity
Let m be the length of nums1, and n be the length of nums2
O(mlogm and nlogn) to sort two arrays by timsort and iterate the two arrays in while loop

Space complexity
With Python sort, O(m + n)
"""


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersect(nums1, nums2))
