from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        middle = (l1 + l2) / 2

        # Edge case when only has one value and either list is empty
        if middle == 0.5:
            return float(nums1[0]) if l1 > l2 else float(nums2[0])

        # Pointers
        x = 0
        y = 0

        #
        cur = 0
        prev = 0

        loops = middle + 1 if middle % 1 == 0 else middle + 0.5

        for _ in range(int(loops)):
            prev = cur

            # When x hits the end of nums1
            if x == l1:
                cur = nums2[y]
                y += 1

            elif y == l2:
                cur = nums1[x]
                x += 1

            elif nums1[x] > nums2[y]:
                cur = nums2[y]
                y += 1

            else:
                cur = nums1[x]
                x += 1

        if middle % 1 == 0.0:
            return (cur + prev) / 2

        else:
            return float(cur)