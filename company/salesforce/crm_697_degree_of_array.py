"""
find degree by counter and max values
sliding window, expand until reaching the degree, once reached degree contract
"""

from typing import List
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        count = collections.defaultdict(int)

        for i, num in enumerate(nums):

            # Save index of first occurrence
            if num not in left:
                left[num] = i

            # Save index of last occurrence by keeping updating it
            right[num] = i

            count[num] += 1

        ans = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                ans = min(right[num] - left[num] + 1, ans)

        return ans


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1]
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(Solution().findShortestSubArray(nums))
