"""
Identify num which has the most frequency
Two pointers
  expand until degree satisfies
    check if currently added num's count
  contract while degree is satisfied
"""

from typing import List
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_to_leftmost = collections.defaultdict(int)
        num_to_rightmost = collections.defaultdict(int)
        num_to_count = collections.defaultdict(int)

        for i in range(len(nums)):
            if nums[i] not in num_to_leftmost:
                num_to_leftmost[nums[i]] = i
            num_to_rightmost[nums[i]] = i
            num_to_count[nums[i]] += 1

        max_count = max(num_to_count.values())

        ans = len(nums)
        for num in num_to_count.keys():
            if num_to_count[num] == max_count:
                ans = min(ans, num_to_rightmost[num] - num_to_leftmost[num] + 1)

        return ans

    def findShortestSubArray1(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        max_count = max(counter.values())

        left = 0

        curr_counter = collections.defaultdict(int)
        ans = len(nums)

        for right in range(len(nums)):

            curr_counter[nums[right]] += 1

            # Contract
            while curr_counter[nums[right]] == max_count:
                ans = min(ans, right - left + 1)
                curr_counter[nums[left]] -= 1
                left += 1

        return ans
