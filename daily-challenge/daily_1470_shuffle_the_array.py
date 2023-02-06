"""
- inplace
"""


from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * len(nums)
        for i in range(n):
            ans[i * 2] = nums[i]
            ans[i * 2 + 1] = nums[i + n]

        return ans


if __name__ == "__main__":
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    # [2, 3, 5, 4, 1, 7]
    print(Solution().shuffle(nums, n))
