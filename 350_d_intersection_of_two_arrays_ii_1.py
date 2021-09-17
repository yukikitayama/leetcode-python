from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        integer_to_count = defaultdict(int)
        for num in nums1:
            integer_to_count[num] += 1
        # print(integer_to_count)

        k = 0
        for num in nums2:
            count = integer_to_count[num]
            if count > 0:
                nums1[k] = num
                k += 1
                integer_to_count[num] = count - 1

        return nums1[:k]


"""
Time complexity
Let m be the length of num1, and n be the length of nums2
O(m) to make hashmap and O(n) to iterate each number, so O(m + n)

Space complexity
O(min(m, n)) to store hashmap
"""


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersect(nums1, nums2))
