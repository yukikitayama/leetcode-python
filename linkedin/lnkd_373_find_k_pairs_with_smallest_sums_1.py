"""
- Initialize count to 0
- Initialize empty list ans
- Initialize two pointers as p1 to 0 and p2 to 0
- While p1 less than nums1 length and p2 less than nums2 length
  - append nums1 at p1 and nums2 at p2 to ans
  - Increment count
  - if nums1 at p1 + 1 is smaller than nums2 at p2 + 1, and
    pointers are not out of bound
    - Increment p1
  - Else
    - Increment p2
  - If count is k
    - break
"""


from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        ans = []
        count = 0
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            ans.append([nums1[p1], nums2[p2]])
            count += 1

            if nums1[p1] < nums2[p2] and p2 != len(nums2) - 1:
                p2 += 1

            elif nums1[p1] < nums2[p2] and p2 == len(nums2) - 1:
                p1 += 1

            elif nums1[p1] >= nums2[p2] and p1 != len(nums1) - 1:
                p1 += 1

            elif nums1[p1] >= nums2[p2] and p1 == len(nums1) - 1:
                p2 += 1

            if count == k:
                break

        return ans


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
# nums1 = [1,2]
# nums2 = [3]
# k = 3
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(Solution().kSmallestPairs(nums1, nums2, k))




