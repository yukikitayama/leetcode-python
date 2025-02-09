"""
sorting descending

[a, b, c]
if c = a + b
a + b + c = c + c = 2c
this means the total sum is double of the one of the item (c)

total = remaining + num + outlier
(remaining + num + outlier) - num - outlier = num, because remaining = num
total - num - num = outlier
"""

from typing import List
import collections


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        counter = collections.Counter(nums)

        ans = float("-inf")
        for num in nums:
            # nums: [2, 3, 5, 10], total: 20
            # num: 5, total - num - num: 20 - 5 - 5 = 10

            # nums: [1, 1, 1, 1, 1, 5, 5], total: 15
            # num: 5, total - num - num: 15 - 5 - 5 = 5
            outlier = total - num - num
            if counter[outlier] > (outlier == num):
                ans = max(ans, outlier)

        return ans