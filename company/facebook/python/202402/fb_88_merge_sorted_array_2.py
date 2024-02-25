from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        for i in range(len(nums1) - 1, -1, -1):

            # Exhausted p2, use p1 but p1 numbers are originally already placed in nums1,
            # so no need to iterate any more
            if p2 < 0:
                break

            # If p1 negative, at else append p2 numbers
            elif p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1

            else:
                nums1[i] = nums2[p2]
                p2 -= 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1

        for i in range(len(nums1) - 1, -1, -1):

            num1 = nums1[p1] if p1 >= 0 else float("-inf")
            num2 = nums2[p2] if p2 >= 0 else float("-inf")

            if num1 > num2:
                nums1[i] = num1
                p1 -= 1
            elif num1 <= num2:
                nums1[i] = num2
                p2 -= 1
