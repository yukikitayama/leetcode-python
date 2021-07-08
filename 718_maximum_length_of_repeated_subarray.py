from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        # memo[i][j] is the longest common prefix of nums1[i:] and nums2[j:]
        memo = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        # print(len(memo), len(memo[0]))
        # print(memo)

        # e.g. len(nums1): 5 -> 4, 3, 2, 1, 0
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1

        [print(row) for row in memo]

        return max(max(row) for row in memo)


nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
# nums1 = [0,0,0,0,0]
# nums2 = [0,0,0,0,0]
print(Solution().findLength(nums1, nums2))