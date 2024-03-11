from typing import List
import collections


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)

        ans = 0

        for i in range(len(nums)):

            if nums[i] not in counter:
                counter[nums[i]] += 1

            else:
                # If we saw current number 3 times before,
                # curent number can form 3 pairs with those previous number seen
                ans += counter[nums[i]]
                counter[nums[i]] += 1

        return ans

