"""
min, max, i, j

(min + max, i + j)
(min + i, j + max)

min + max >= min + i
j + i <= j + max

j + i -- j + max -- min + i -- min + max
"""


from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        ascending = sorted(nums)
        descending = sorted(nums, reverse=True)

        ans = float('-inf')
        for a, b in zip(ascending, descending):
            ans = max(ans, a + b)

        return ans


if __name__ == '__main__':
    nums = [3, 5, 2, 3]
    print(Solution().minPairSum(nums))
