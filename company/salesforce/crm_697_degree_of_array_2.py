"""
counter to find degree

two pointer
expand when current degree is not the array degree
contract when current degree is the array degree
"""

from typing import List
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)

        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i

        degree = max(counter.values())
        ans = float("inf")
        for k in counter:
            if counter[k] == degree:
                ans = min(ans, right[k] - left[k] + 1)

        return ans


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1]
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(Solution().findShortestSubArray(nums))
