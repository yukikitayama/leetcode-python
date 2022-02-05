"""
- Iterate from end?
- 3 pointers
  - num2 index
  - num1 index
  - insert index
"""


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1

        for i in range(n + m - 1, -1, -1):

            # No need to update any more because we can use the original numbers in nums1
            if p2 < 0:
                break

            # p1 >= 0 because when pointer gets negative, it points the end of array
            # Negative p1 also mean we used up all the nums1, so we can always nums2 number
            # in the below else block
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1

            else:
                nums1[i] = nums2[p2]
                p2 -= 1

        print(nums1)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    # [1, 2, 2, 3, 5, 6]
    print(Solution().merge(nums1, m, nums2, n))
