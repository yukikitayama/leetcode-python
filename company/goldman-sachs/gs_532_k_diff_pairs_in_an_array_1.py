"""
- Take O(n^2) to make a pair
- TLE
"""


from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s_nums = sorted(nums)

        ans = 0

        for i in range(len(s_nums)):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue

            for j in range(i + 1, len(s_nums)):
                if j > i + 1 and s_nums[j] == s_nums[j - 1]:
                    continue

                if abs(s_nums[j] - s_nums[i]) == k:
                    ans += 1

        return ans


nums = [3,1,4,1,5]
k = 2
# 2
nums = [1,2,3,4,5]
k = 1
# 4
nums = [1,3,1,5,4]
k = 0
# 1
nums = [1,2,4,4,3,3,0,9,2,3]
k = 3
# 2
nums = [-1,-2,-3]
k = 1
# 2
print(Solution().findPairs(nums, k))

