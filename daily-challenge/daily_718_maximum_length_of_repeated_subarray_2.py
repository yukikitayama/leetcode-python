"""
- 4 pointers 2 sliding windows
"""


from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        ans = 0

        for p1 in range(len(nums1) - 1, -1, -1):

            for p2 in range(len(nums2) - 1, -1, -1):

                if nums1[p1] == nums2[p2]:

                    dp[p1][p2] = dp[p1 + 1][p2 + 1] + 1

                    ans = max(ans, dp[p1][p2])

        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    print(Solution().findLength(nums1, nums2))
