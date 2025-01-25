"""
this swapping is transitive: If a can swap with b, and b can swap with c, then a can effectively be swapped with c.

we want to organize nums into groups, so that all elements in a given group can participate in this transitive chaining and can thus be reordered in our desired increasing order.
"""

from typing import List
import collections


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)

        curr_group = 0
        num_to_group = {}
        num_to_group[sorted_nums[0]] = curr_group

        group_to_nums = collections.defaultdict(collections.deque)
        group_to_nums[curr_group].append(sorted_nums[0])

        for i in range(1, len(sorted_nums)):

            if abs(sorted_nums[i - 1] - sorted_nums[i]) > limit:
                curr_group += 1

            num_to_group[sorted_nums[i]] = curr_group

            group_to_nums[curr_group].append(sorted_nums[i])

        ans = [None] * len(nums)
        for i in range(len(nums)):
            group = num_to_group[nums[i]]
            ans[i] = group_to_nums[group].popleft()

        return ans