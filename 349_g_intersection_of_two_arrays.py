from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    def set_intersection(self, set1: set, set2: set) -> List[int]:
        return [x for x in set1 if x in set2]


"""
Time complexity
Let m be the length of nums1, and n be the length of nums2
O(m) to make set1, O(n) to make set2, set_intersection takes O(n or m)
so O(n + m)

Space complexity
O(m + n) for two sets
"""


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))
