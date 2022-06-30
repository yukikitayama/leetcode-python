"""
- Sum of absolute difference between current number and median
"""


from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        ans = 0
        nums.sort()

        for i in range(len(nums)):
            ans += abs(nums[i] - nums[mid])

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [1, 2, 3, 4]
    # 4 for 2, 4 for 3, even length no median existing array works too
    print(Solution().minMoves(nums))
